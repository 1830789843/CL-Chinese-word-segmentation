# class TrieNode:
# 	def __init__(self):
# 		self.value = None
# 		self.data = {}    # children is of type {char, Node}
# 		self.is_word = False
#
# class Trie:
#
# 	def __init__(self):
# 		"""
# 			Initialize your data structure here.
# 		"""
# 		self.root = TrieNode()
#
# 	def insert(self, word):
# 		"""
# 		Inserts a word into the trie.
# 		:type word: str
# 		:rtype: void
# 		"""
# 		node = self.root
# 		for chars in word:
# 			child = node.data.get(chars)
# 			if not child:
# 				node.data[chars] = TrieNode()
# 			node = node.data[chars]
# 		node.is_word = True
#
# 	def search(self, word):
# 		"""
# 		Returns if the word is in the trie.
# 		:type word: str
# 		:rtype: bool
# 		"""
# 		node = self.root
# 		for chars in word:
# 			node = node.data.get(chars)
# 			if not node:
# 				return False
# 		return node.is_word  # 判断单词是否是完整的存在在trie树中
#
# 	def startsWith(self, prefix):
# 		"""
# 		Returns if there is any word in the trie that starts with the given prefix.
# 		:type prefix: str
# 		:rtype: bool
# 		"""
# 		node = self.root
# 		for chars in prefix:
# 			node = node.data.get(chars)
# 			if not node:
# 				return False
# 		return True
#
# 	def get_start(self, prefix):
# 		"""
# 		  Returns words started with prefix
# 		  :param prefix:
# 		  :return: words (list)
# 		"""
#
# 		def get_key(pre, pre_node):
# 			word_list = []
# 			if pre_node.is_word:
# 				word_list.append(pre)
# 			for x in pre_node.data.keys():
# 				word_list.extend(get_key(pre + str(x), pre_node.data.get(x)))
# 			return word_list
#
# 		words = []
# 		if not self.startsWith(prefix):
# 			return words
# 		if self.search(prefix):
# 			words.append(prefix)
# 			return words
# 		node = self.root
# 		for chars in prefix:
# 			node = node.data.get(chars)
# 		return get_key(prefix, node)
#
# # trie = Trie()
# # trie.insert('hello')
# # trie.insert('nice')
# # trie.insert('to')
# # trie.insert('meet')
# # trie.insert('you')
# # print(trie.search('hello'))
# # print(trie.search('HELLO'))
#
# trie = Trie()
# trie.insert("something")
# trie.insert("somebody")
# trie.insert("somebody1")
# trie.insert("somebody3")
# print(trie.search("key"))
# print(trie.search("somebody3"))
# print(trie.get_start('some'))

# 按行读文件
dic_file = open("../wordCount2.txt", 'r', encoding='gbk')
freq_dict = {}
for l in dic_file:
	# [0: len-1]用于去换行符号
	len = l.split(' ')[1].__len__()
	freq_dict[l.split(' ')[0]] = l.split(' ')[1][0: len-1]
	# break
dic_file.close()
