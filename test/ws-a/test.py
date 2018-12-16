# -*- coding: utf-8 -*-
import numpy as np
#
# wordCountDic = {}
#
# with open("../testW.txt", 'r', encoding='gbk') as file:
#     # word_count(file, wordCountDic)
#     # print(file.read())
#     content = file.read()
#
#     for part in content.split("  "):
#         part = part[0: part.find("/")]
#         wordCountDic[part] = 1
#
# print(wordCountDic)
#
# with open("../testWordCount.txt", 'w') as file:
#     for key, value in wordCountDic.items():
#         file.write('{key} {value}\n'.format(key=key, value=value))
#
# from wordCount import wordCountDic, count_total, wordProbability
#
# print(wordCountDic.items())
# print(count_total)
# print(wordProbability['希望'])
# if "希望" in wordCountDic.keys():
#     print('{key} {value}\n'.format(key=key, value=wordCountDic[key]))
#
# a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# b = np.array([2, 2, 2])
# c = a - b
# print(c)
# a = np.sum([1, 2, 3])
# print(a)
#
# a = "sssssasdsss"
# index = a.find("a")
# temp = a[0: index]
# print(temp)
# temp = a[index:]
# print(temp)
#
# word_list = ['他', '们', '有', '意', '见', '分', '他们', '有意', '意见', '分歧']
#
# for c in word_list:
#     temp = word_list.index(c)
#     print(temp)

dic = {1: [1, 2, 3]}
dic2 = {2: [3, 4]}
dic3 = {3: [4, 5]}
word = {1: True, 2: True, 3: True}
# value = word[dic.keys()[0]]
# print(value)

# list2 = ["a", "v"]
# temp = ''.join(list2)
# a = "ab"
# b = list(a)
# print(b)
# # temp = np.array(list2)
# # temp.
# # key = temp.tostring()
# print(temp)

dic = {" 她": True, " 他": False}
valur = dic[" 她"]
print(valur)
print(dic.keys())

# temp = []
# temp2 = np.array(temp)
# print(temp)
# print(temp2)
# temp.append("s")
# print(temp)
# print(temp2)
# temp = list(temp2)
# print(temp)

#
# def is_exist(part, temp_list):
# 	flag = False
# 	result_list = []
# 	for e in temp_list:
# 		for p in part:
# 			if e.find(p) != -1:
# 				flag = True
# 			else:
# 				result_list.append(e)
# 	return flag, result_list
#
# word_list = ['有', '意', '见', '分', '有意', '意见', '分歧']
# a, b = is_exist("意", word_list)
# print(a)
# print(b)

# result_list = []
# dic = {'有': {-1: True, '意': {-1: True}, '意见': {-1: True}, '有意': {'见': {-1: True}, '分': {-1: True}, '分歧': {-1: True}}}, '有意': {-1: True}}
# dic = {-1: True, '意': {-1: True}, '意见': {-1: True}, '有意': {'见': {-1: True}, '分': {-1: True}, '分歧': {-1: True}}}
#
# result_list = []
# def get_all(dic):
# 	if dic is None:
# 		return None
#
# 	if dic.__len__() == 1:
# 		return None
#
# 	for key, value in dic.items():
# 		if key != -1:
# 			print("!!!!!!")
# 			result_list.append(key)
# 			# print(result_list)
# 			# print(dic.get(key))
# 			# print(get_all(dic.get(key)))
# 			result_list.append(get_all(dic.get(key)))
# 			# print(result_list)
# 	return result_list
#
#
# print(get_all(dic))
#
# dic = {'分歧': {-1: True}}
# print(dic.__len__())
# print(str(dic))
# print(list(dic.keys())[0])

# 获取所有标点符号等
# 定义标点符号列表
# punctuation_list = []
# with open("../词性标注%40人民日报199801.txt", 'r', encoding='utf-8') as file:
# 	content = file.read()
# 	for line in content.split("\n"):
# 		index = line.find("/w")
# 		part = line[index-1: index]
# 		if part not in punctuation_list:
# 			punctuation_list.append(part)
# 		print(part)
#
# print(punctuation_list)

# 测试global的用法
# s = 7
#
# def test():
# 	global s
# 	print(s)
#
# test()

# 对字典按键排序
candidate_word_list = {'0 他们': [], '2 有意': ['0 他们'], '4 见': ['2 有意'], '5 分歧': ['4 见', '3 意见'], '3 意见': ['2 有'], '2 有': ['0 他们']}
sorted(candidate_word_list.keys())
print(sorted(candidate_word_list.keys()))
