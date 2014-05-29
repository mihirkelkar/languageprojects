#!/usr/bin/python
import sys
class node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

class bstree:
	def __init__(self, value):
		self.root = node(value)
		self.inorder = []
	def add_node(self, value, root = None):
		root = self.root if root is None else root
		if root.value > value:
			if root.left != None:
				self.add_node(value, root.left)
			else:
				print "Adding node to left"
				root.left = node(value)
		elif root.value <= value:
			if root.right != None:
				self.add_node(value, root.right)
			else: 
				print "Adding node to right"
				root.right = node(value)

	
	def find_nth_largest(self, n, root = None):
		root = self.root if root is None else root
		if root.left != None:
			self.find_nth_largest(n, root.left)
		self.inorder.append(root.value)
		if len(self.inorder) == n:
			print self.inorder[-1]

		if root.right != None:
			self.find_nth_largest(n, root.right)
		
			
				




def main():
	tree = bstree(1)
	tree.add_node(2)
	tree.add_node(3)
	tree.add_node(4)
	tree.add_node(5)
	tree.add_node(6)
	tree.find_nth_largest(6)

if __name__ == "__main__":
	main()
				
		
