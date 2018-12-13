# -*- coding: utf-8 -*-
# 计算词频和概率，并写入文件

# 定义的三个全局变量中只有两个字典是有值的。count_total还是0
wordCountDic = {}
count_total = 0
wordProbability = {}


# 计算根据语料库计算词频与词的概率
def word_count(content, bg_word):
	for line in content.split("\n"):
		for part in line.split("  "):
			part = part[0: part.find("/")]
			if part in bg_word:
				bg_word[part] += 1
			else:
				bg_word[part] = 1
	count_total = 0
	# return word count dictionary
	with open("../wordCount.txt", 'w') as file:
		for key, value in bg_word.items():
			count_total += value
			file.write('{key} {value}\n'.format(key=key, value=value))
		print(count_total)
	with open("../wordProbability.txt", 'w') as file:
		for key, value in bg_word.items():
			p ='{:.8f}'.format(value/count_total)
			wordProbability[key] = p
			file.write('{key} {value}\n'.format(key=key, value=p))
	return bg_word


with open("../词性标注%40人民日报199801.txt", 'r', encoding='utf-8') as file:
	content = file.read()
	word_count(content, wordCountDic)
