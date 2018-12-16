# -*- coding: utf-8 -*-
# 这里的平滑与获取候选词时不对
import re

# 定义词典word_dic
word_dic = {}
word_count_list = {}
word_probability = {}
count_total = 0
# 定义更新次数
count = 0


# 获取字典：词:词频-总词数-词频
def get_word_dic():
	global word_dic
	global word_count_list
	global word_probability
	global count_total
	# 定义词频字典，概率字典，总词数
	with open("../词性标注%40人民日报199801.txt", 'r', encoding='utf-8') as file:
		train_txt = file.read()
	for line in train_txt.split("\n"):
		for part in line.split("  "):
			part = part[0: part.find("/")]
			count_total += 1
			if part in word_count_list:
				word_count_list[part] += 1
			else:
				word_count_list[part] = 1
	with open("../word_dic.txt", 'w') as file:
		for key, value in word_count_list.items():
			p ='{:.8f}'.format(value/count_total)
			word_probability[key] = p
			file.write('{key}:{value1}  {value2}  {value3}\n'.format(key=key, value1=value, value2=count_total, value3=p))
			keyAll = str(value) + '  ' + str(count_total) + '  ' + str(p)
			word_dic[key] = keyAll
	return word_dic


# 判断词典中是否有某个字。没有这个字，就一定得加入词典
# 没有找到返回false.找到返回true
def is_exist(word, word_dic):
	flag = False
	for key in word_dic.keys():
		# 如果找到，则false
		if key.find(word) != -1:
			flag = True
			break

	return flag


# 加1平滑-当某个字不在词典中时，加入。此时更新词典
def update_word_dic(temp):
	global count
	global count_total
	global word_dic
	global word_count_list
	global word_probability
	global count_total
	path = "../word_dic"+str(count)+".txt"
	count += 1
	count_total += 1
	# 将新词加入，并写入词典文件
	word_count_list[temp] = 1
	with open(path, 'w') as file:
		for key, value in word_count_list.items():
			if key != temp:
				word_count_list[key] += 1
				value = word_count_list[key]
			# 概率保留8位小数点
			p ='{:.8f}'.format(value/count_total)
			word_probability[key] = p
			file.write('{key}:{value1}  {value2}  {value3}\n'.format(key=key, value1=value, value2=count_total, value3=p))
			keyAll = str(value) + '  ' + str(count_total) + '  ' + str(p)
			word_dic[key] = keyAll
	return word_dic


# 获取所有候选词。此处，加入平滑。并存入字典 {"出现位置 候选词"：概率}
def get_word_list(sentence, max_word_list_count):
	word_list = {}
	len = sentence.__len__()
	# 定义划分长度，从1 到max_word_list_count
	for i in range(1, max_word_list_count + 1, 1):
		for j in range(len):
			if j + i <= len:
				temp = sentence[j: j + i]
			else:
				temp = sentence[j: len + 1]
			# 若单个字不在词典中，则加入，用加1平滑处理
			if temp not in word_count_list.keys():
				if i == 1 and is_exist(temp, word_dic) is False:
					# 平滑--更新词典
					update_word_dic(temp)
					word_list[str(j)+" "+temp] = word_probability[temp]
			else:
				if temp not in word_list:
					word_list[str(j)+" "+temp] = word_probability[temp]
			if temp in word_count_list.keys():
				if temp not in word_list:
					word_list[str(j)+" "+temp] = word_probability[temp]
	return word_list


# 找到所有候选词的所有左邻词，存入字典{"出现位置 词":[左邻词,左邻词...]}
def find_left_word(word_list, sentence):
	left_word_list = {}
	for key, value in word_list.items():
		left_word_list[key] = []
		# 从该词前面找左邻词。先找到该词出现的位置。如果某词中包含该词的前一个字，并且某词的index正确，则为左邻词
		index = int(key.split(" ")[0])
		if index == 0:
			left_word_list[key] = []
		else:
			temp = sentence[(index-1): index]
			for now in word_list.keys():
				current_index = int(now.split(" ")[0])
				current_word = now.split(" ")[1]
				len = current_word.__len__()
				if current_word[len-1:len] == temp and current_index + len == index:
					if key in left_word_list:
						left_word_list[key].append(now)
					else:
						left_word_list[key].append(now)
	return left_word_list


# 计算每个词的累计概率，与最佳左邻词。存入字典：{"出现位置 词"：概率++最佳左邻词}
def find_best_left_word(left_word_list, word_list):
	best_left_word_list = {}
	for key, value in left_word_list.items():
		if value is []:
			best_left_word_list[key] = str(word_list[key]) + "++" + ""
		else:
			temp_left_word_list = value
			max_probability = 0.0
			best_left_word = ""
			for cur_left_word in temp_left_word_list:
				if max_probability <= float(word_list[key]) * float(word_list[cur_left_word]):
					if left_word_list[cur_left_word] == [] and cur_left_word[0] != "0":
						continue
					max_probability = float(word_list[key]) * float(word_list[cur_left_word])
					best_left_word = cur_left_word
			best_left_word_list[key] = str(max_probability) + "++" + best_left_word
	print(best_left_word_list)
	return best_left_word_list


# 反向查找最佳左邻词，返回切分结果
def get_result(sentence, best_left_word_list):
	# 先找到最后一个词
	word = sentence[-1]
	result = ''
	if word != '' and word != "\n":
		last_word = ''
		max_probability = 0.0
		for key, value in best_left_word_list.items():
			current_word = key.split(" ")[1]
			probability = float(value.split("++")[0])
			if current_word[-1] == word and max_probability <= probability:
				max_probability = probability
				last_word = key
		result = last_word.split(" ")[1]
		best_left_word = best_left_word_list[last_word].split("++")[1]
		while best_left_word != "":
			result = best_left_word.split(" ")[1] + " " + result
			best_left_word = best_left_word_list[best_left_word].split("++")[1]
	return result


# 定义分词算法
def segmentation(sentence):
	# 定义划分最大词长度
	max_word_list_count = 10
	word_list = get_word_list(sentence, max_word_list_count)
	left_word_list = find_left_word(word_list, sentence)
	best_left_word_list = find_best_left_word(left_word_list, word_list)
	result = get_result(sentence, best_left_word_list)
	return result


get_word_dic()
# 使用正则表达式。将所有句子根据各种标点符号划分。有可能句子前后都有标点。则判断整行前有没有标点，剩下的在句子后判断
pattern = r',|\.|/|;|\'|`|\[|\]|<|>|\?|:|"|\{|\}|\~|!|@|#|\$|%|\^|&|\(|\)|-|=|\_|\+|，|。|、|；|‘|’|【|】|！| |…|（|）|●'

# with open("../test.txt", "r", encoding="gbk") as file:
# 	with open("../result_3.txt", 'w') as result_file:
# 		test_text = file.read()
# 		# 按照每一行处理
# 		for line in test_text.split("\n"):
# 			# 如果该行不为空，且第一位为标点，则写入文件
# 			if line != "" and pattern.find(line[0]) != -1:
# 				result_file.write(line[0] + " ")
# 			sentence_list = re.split(pattern, line[0: line.__len__()])
# 			for sentence in sentence_list:
# 				if sentence == "" or sentence == "\n":
# 					continue
# 				result_file.write(segmentation(sentence))
# 				index = line.find(sentence)
# 				len = sentence.__len__()
# 				punctuation = line[index+len:index+len+1]
# 				if punctuation != " ":
# 					result_file.write(" ")
# 					result_file.write(punctuation)
# 				result_file.write(" ")
# 			result_file.write("\n")

# print(segmentation("认真汲取东南亚金融风波教训"))
print(segmentation("他们有意见分歧"))
# print(segmentation("这次会议是１２日召开的。"))
