# -*- coding: utf-8 -*-
# 定义trie树，使用字典的嵌套实现树
import numpy as np

class Trie:
	def __init__(self):
		self.root = {}
		self.end = -1

	def insert(self, word):
		"""
		Inserts a word into the trie.
			:type word: list
			:rtype: void
		"""
		curNode = self.root
		for c in word:
			if not c in curNode:
				curNode[c] = {}
			curNode = curNode[c]
		curNode[self.end] = True

	def search(self, word):
		"""
		Returns if the word is in the trie.
		:type word: list
		:rtype: bool
		"""
		curNode = self.root
		for c in word:
			if not c in curNode:
				return False
			curNode = curNode[c]

		# Doesn't end here
		if not self.end in curNode:
			return False
		return True

	def startsWith(self, prefix):
		"""
		Returns if there is any word in the trie that starts with the given prefix.
		:type prefix: list
		:rtype: bool
		"""
		curNode = self.root
		for c in prefix:
			if not c in curNode:
				return False
			curNode = curNode[c]

		return True

	# 判断temp-list中是否已经包含part，如果包含则剔除包含part的元素，返回一个result_list
	def is_exist(self, part, temp_list):
		flag = False
		result_list = []
		for e in temp_list:
			for p in part:
				if e.find(p) != -1:
					flag = True
					break
				result_list.append(e)
				break

		return flag, result_list

	# str是截至现在的串，temp_list是当前的list.返回能完全匹配str的list
	def is_all(self, str, temp_list):
		return result_list

	# 获取当前trie的所有路径
	def get_all(self, dic):
		result_list = []
		if dic is None:
			return []

		def recursive(dic, temp=''):
			if dic.__len__() == 1:
				result_list.append(temp)

			for key, value in dic.items():
				temp2 = temp
				if key != -1:
					temp += str(key)
					temp += ' '
					recursive(dic.get(key), temp)
				temp = temp2
		recursive(dic)  # 调用递归
		return result_list


# Your Trie object will be instantiated and called as such:
# word_list = ['提', '高', '人', '民', '生', '活', '水', '平', '提高', '高人', '人民', '民生', '生活', '活水', '水平']

word_list = ['他', '们', '有', '意', '见', '分', '他们', '有意', '意见', '分歧']
word_list = ['有', '意', '见', '分', '有意', '意见', '分歧']
# text = "提高人民生活水平"
text = "他们有意见分歧"
text = "有意见分歧"
obj = Trie()
# dic。已经处理好的
temp2 = {}
count = 0
temp = []
for i in range(text.__len__()):
	# print(text[i])
	# 用于存储接下来的每个词的候选词
	temp_list = []
	# temp2.append(text[i])
	# temp = temp2
	print(obj.root)

	# temp2 = list(obj.root.keys())
	for j in range(word_list.__len__()):
		if word_list[j].startswith(text[i]):
			print("222222222")
			# flag, result_list = obj.is_exist(word_list[j], temp2)
			# temp = result_list
			# 根据以往已经分好的，添加该节点，再插入
			print(temp)
			temp.append(word_list[j])
			temp_list.append(word_list[j])
			if not obj.search(temp):
				# print(temp)
				obj.insert(temp)
			temp = list(temp2)
			# break
	# break

print(obj.root)

res = obj.get_all(obj.root)
print(res)

