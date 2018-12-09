# -*- coding: utf-8 -*-
from wordCount import wordCountDic, count_total, wordProbability

text = "他们有意见分歧"
# text = "提高人民生活水平"

# 将txt转换为列表
def pre_data(text):
	content = []
	len = text.__len__()
	for i in range(len):
		content.append(text[i: i+1])
	return content

def get_word_list(content, max_word_list_count):
	word_list = []
	len = content.__len__()
	for i in range(max_word_list_count):
		for j in range(len):
			if j + i < len:
				temp = content[j : j + i + 1]
			else:
				temp = content[j: len]
			if temp in wordCountDic.keys():
				if temp not in word_list:
					word_list.append(temp)
	return word_list

def MP(word_list):
	result_list = []

	return result_list

def fenci(txt):
	max_word_list_count = 3
	content = pre_data(txt)
	word_list = get_word_list(content, max_word_list_count)
	result_list = MP(word_list)
	return  result_list

# 暂时没用到
content = pre_data(text)
print(content)
word_list = get_word_list(text, 3)
print(word_list)
