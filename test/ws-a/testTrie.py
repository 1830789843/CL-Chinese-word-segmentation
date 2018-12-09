# -*- coding: utf-8 -*-
class Trie:

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.root = {}
		self.end = -1

	def insert(self, word):
		"""
		Inserts a word into the trie.
		:type word: []list
		:rtype: void
		"""
		curNode = self.root
		temp = ""
		for c in word:
			temp += c
			if not c in curNode:
				curNode[c] = {}
			curNode = curNode[c]
		# print(temp)
		curNode = curNode[temp]
		curNode[self.end] = True

	def search(self, word):
		"""
		Returns if the word is in the trie.
		:type word: str
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
		:type prefix: str
		:rtype: bool
		"""
		curNode = self.root
		for c in prefix:
			if not c in curNode:
				return False
			curNode = curNode[c]

		return True


# Your Trie object will be instantiated and called as such:
# word_list = ['提', '高', '人', '民', '生', '活', '水', '平', '提高', '高人', '人民', '民生', '生活', '活水', '水平']

word_list = ['他', '们', '有', '意', '见', '分', '他们', '有意', '意见', '分歧']
# text = "提高人民生活水平"
text = "他们有意见分歧"
obj = Trie()
for i in range(text.__len__()):
	# print(text[i])
	temp_list = []
	temp = []
	for j in range(word_list.__len__()):
		if word_list[j].find(text[i]):
			temp_list.append(word_list[j])
			index = text.find(word_list[j])
			print(index)
			temp.append(text[0: index])
			temp.append(word_list[j])
			if not obj.search(temp):
				print(temp)
				break
				obj.insert(temp)
			temp = ""

print(obj.root)
