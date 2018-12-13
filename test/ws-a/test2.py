# -*- coding: utf-8 -*-
import numpy as np

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
        temp = []
        key = ""
        dic = {}
        print("start")
        i = 1
        for c in word:
            if not c in curNode:
                curNode[c] = {}
            curNode = curNode[c]
        # curNode = curNode[c]
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


obj = Trie()
obj.insert("他们呢")

print(obj.root)


