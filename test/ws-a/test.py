# -*- coding: utf-8 -*-
import numpy as np
wordCountDic = {}

with open("../test.txt", 'r', encoding='gbk') as file:
	# word_count(file, wordCountDic)
	# print(file.read())
	content = file.read()

	for part in content.split("  "):
		part = part[0: part.find("/")]
		wordCountDic[part] = 1

print(wordCountDic)

with open("../testWordCount.txt", 'w') as file:
	for key, value in wordCountDic.items():
		file.write('{key} {value}\n'.format(key = key, value = value))


from wordCount import wordCountDic, count_total, wordProbability
print(wordCountDic.items())
print(count_total)
print(wordProbability['希望'])
if "希望" in wordCountDic.keys():
	print('{key} {value}\n'.format(key=key, value=wordCountDic[key]))

# a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# b = np.array([2, 2, 2])
# c = a - b
# print(c)
# a = np.sum([1, 2, 3])
# print(a)

a = "sssssasdsss"
index = a.find("a")
temp = a[0: index]
print(temp)
temp = a[index:]
print(temp)

word_list = ['他', '们', '有', '意', '见', '分', '他们', '有意', '意见', '分歧']

for c in word_list:
	temp = word_list.index(c)
	print(temp)