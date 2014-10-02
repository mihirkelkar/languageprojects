#!/usr/bin/python

CHECKER_ARRAY = list()

class Node(obejct):
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class BSTree(obejct):
  def __init__(self):
    self.head = None

  def add_node(self, value, root = None):
    root = self.root if root is None else root
    if self.root == None:
      self.root = Node(value)
    else:
      if value <= root.value:
        if root.left != None:
          self.add_node(value, root.left)
        else:
          root.left = Node(value)
      else:
        if root.right != None:
          self.add_node(value, root.right)
        else:
          root.right = Node(value)

  def check_if_bst(self, root = None):
    root = self.root if root is None else root
    if root.left != None:
      self.check_if_bst(root.left)
    CHECKER_ARRAY.append(root.value)
    if root.right != None:
      self.check_if_bst(root.right)


def main():
  #Build a tree here again. 
  tree.check_if_bst()
  if CHECKER_ARRAY == CHECKER_ARRAY.sort():
    print "This is a binary search tree. "
  else:
    print "This is not a binary search tree"    
