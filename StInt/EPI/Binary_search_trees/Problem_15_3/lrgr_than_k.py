#!/usr/bin/python

class Node(object):
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
  

class BST(object):
  def __init__(self):
    self.root = None
    self.list = list()

  def add_node(self,value, root = None):
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

  def larger_than_k(self, value, root = None):  
