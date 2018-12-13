# -*- coding: utf-8 -*-
# 返回一个树的所有根到叶的路径
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

	def binaryTreePaths(self, root):
		"""
		:type root: TreeNode
		:rtype: List[str]
		"""
		if not root:  # 为空，直接返回[]
			return []
		res = []

		# temp=''

		def recursive(root, temp=''):
			# global temp
			temp += str(root.val)
			if not root.left and not root.right:  # 左右子树皆为空时
				res.append(temp)
			temp += '->'
			if root.left:
				recursive(root.left, temp)
			if root.right:
				recursive(root.right, temp)

		recursive(root)  # 调用递归
		return res


node = TreeNode("A")
node1 = TreeNode("B")
node2 = TreeNode("C")
node3 = TreeNode("D")
node4 = TreeNode("E")
node.left = node1
node.right = node4
node1.left = node2
node1.right = node3


solution = Solution()
print(solution.binaryTreePaths(node))
