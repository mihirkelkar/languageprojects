#!/usr/bin/python

class Node(object):
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
 
class Tree(object):
  def __init__(self):
    self.root = None
    self.inorder_list = list()

  def make_list_inorder_traversal(self, root = None):
    root = self.root if root is None else root
    if root.left != None:
      self.make_list_inorder_traversal(root.left)
    self.inorder_list.append(root.value)
    if root.right != None:
      self.make_list_inorder_traversal(root.right)

  def make_bst(self, root = None):
    root = self.root if root is None else root
    if root.left != None:
      self.make_bst(root.left)
    root.value = self.inorder_list.pop(0)
    if root.right != None:
      self.make_bst(root.right)

def main():
  btree = Tree()
  btree.root = Node(10)
  btree.root.left = Node(2)
  btree.root.right = Node(7)
  btree.root.left.left = Node(8)
  btree.root.left.right = Node(4)
  btree.make_list_inorder_traversal()
  btree.inorder_list.sort()
  btree.make_bst()
  btree.make_list_inorder_traversal()
  print btree.inorder_list

if __name__ == "__main__":
  main()
