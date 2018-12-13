# -*- coding: utf-8 -*-
# 定义trie树。使用树节点来实现
class TrieNode:
	def __init__(self):
		self.value = None
		self.data = {}    # children is of type {char, Node}
		self.is_word = False

class Trie:

	def __init__(self):
		"""
			Initialize your data structure here.
		"""
		self.root = TrieNode()

	def insert(self, word):
		"""
		Inserts a word into the trie.
		:type word: list
		:rtype: void
		"""
		node = self.root
		for chars in word:
			child = node.data.get(chars)
			if not child:
				node.data[chars] = TrieNode()
			node = node.data[chars]
		node.is_word = True

	def search(self, word):
		"""
		Returns if the word is in the trie.
		:type word: str
		:rtype: bool
		"""
		node = self.root
		for chars in word:
			node = node.data.get(chars)
			if not node:
				return False
		return node.is_word  # 判断单词是否是完整的存在在trie树中

	def startsWith(self, prefix):
		"""
		Returns if there is any word in the trie that starts with the given prefix.
		:type prefix: str
		:rtype: bool
		"""
		node = self.root
		for chars in prefix:
			node = node.data.get(chars)
			if not node:
				return False
		return True

	def get_start(self, prefix):
		"""
			Returns words started with prefix
			:param prefix:
			:return: words (list)
		"""

		def get_key(pre, pre_node):
			word_list = []
			if pre_node.is_word:
				word_list.append(pre)
			for x in pre_node.data.keys():
				word_list.extend(get_key(pre + str(x), pre_node.data.get(x)))
			return word_list

		words = []
		if not self.startsWith(prefix):
			return words
		if self.search(prefix):
			words.append(prefix)
			return words
		node = self.root
		for chars in prefix:
			node = node.data.get(chars)
		return get_key(prefix, node)


# Your Trie object will be instantiated and called as such:

word_list = ['他', '们', '有', '意', '见', '分', '他们', '有意', '意见', '分歧']
word_list = ['有', '意', '见', '分', '有意', '意见', '分歧']
text = "他们有意见分歧"
text = "有意见分歧"
obj = Trie()
# dic。已经处理好的
temp2 = {}
count = 0
temp = []
for i in range(text.__len__()):
	print(text[i])
	# 用于存储接下来的每个词的候选词
	temp_list = []
	# temp2.append(text[i])
	# temp = temp2
	print(obj.root.data)
	# temp2 = list(obj.data.keys())
	for j in range(word_list.__len__()):
		if word_list[j].startswith(text[i]):
			print("222222222")
			# flag, result_list = obj.is_exist(word_list[j], temp2)
			# temp = result_list
			print(temp)
			temp.append(word_list[j])
			temp_list.append(word_list[j])
			if not obj.search(temp):
				print(temp)
				obj.insert(temp)
			temp = list(temp2)
			# break
	# break

# obj = Trie()
# obj.insert(["它", "们"])
print(obj)
