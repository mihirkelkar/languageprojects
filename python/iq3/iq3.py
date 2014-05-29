#!/usr/bin/python

class double_ll_node:
	def __init__(self, value):
		self.value = value
		self.prev = None
		self.nxt = None

class double_ll:
	def __init__(self, value):
		self.head = double_ll_node(value)
		self.tail = self.head
	def add_node(self, value):
		self.tail.nxt = double_ll_node(value)
		self.tail.nxt.prev = self.tail
		self.tail = self.tail.nxt

	def print_ll(self):
		cur = self.head
		while(cur != None):
			print cur.value
			cur = cur.nxt
		



class node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
	
class bstree:
	def __init__(self, value):
		self.root = node(value)
		self.inorderlist = []
	def add_node(self, value, root = None):
		root = self.root if root is None else root
		if value <= root.value:
			if root.left != None:
				self.add_node(value, root.left)
			else:
				root.left = node(value)
		elif value > root.value:
			if root.right != None:
				self.add_node(value, root.right)
			else:
				root.right = node(value)
	def inorder(self, root = None):
		root = self.root if root is None else root
		if root.left != None:
			self.inorder(root.left)
		self.inorderlist.append(root.value)
		if root.right != None:
			self.inorder(root.right)
	def convert(self):
		#print self.inorderlist
		dll = double_ll(self.inorderlist[0])
		for i in self.inorderlist[1:]:
			dll.add_node(i)
		
		dll.print_ll()		


def main():
	tree = bstree(1)
	for i in range(2, 10):
		#print i
		tree.add_node(i)
	tree.inorder()
	tree.convert()

if __name__ == "__main__":
	main()
