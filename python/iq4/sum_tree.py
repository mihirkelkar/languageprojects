#!/usr/bin/python

class node:
	def __init__(self, value):
		self.value = value
		self.left = None	
		self.right = None


class btree:
	def __init__(self, value):
		self.root = node(value)
	def add_node(self, value, root = None):
		root = self.root if root is None else root
		if value <= root.value:
			if root.left != None:
				self.add_node(value, self.left)
			else:
				root.left = node(value)
		elif value > root.value:
			if root.right != None:
				self.add_node(value, self.right)
			else:
				root.right = node(value)

	def c_sumtree(self, root = None):
		root = self.root if root is None else root
		if root.left != None:
			left = self.c_sumtree(root.left)
		else:
			left = 0
		if root.right != None:
			right = self.c_sumtree(root.right)
		else:
			right = 0
		temp = root.value
		root.value = left + right
		return temp

		

