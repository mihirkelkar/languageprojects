#!/usr/bin/python

class Node(object):
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
    self.lsc = 0

class BTree(object):
  def __init__(self):
    self.root = None
  
  def add_node(self, value, root = None):
    root = self.root if root is None else root
    if value <= root.value:
      if root.left != None:
        self.add_node(value, root.left)
      else:
        root.left = Node(value)
      root.lsc += 1
    elif value > root.value:
      if root.right != None:
        self.add_node(value, root.right)
      else:
        root.right = Node(value)
      root.lsc += 1

  def find_kth_element_inorder(self, k, root = None):
    root = self.root if root is None else root
    if k == root.lsc + 1
      print root.value
    elif k <= root.lsc:
      self.find_kth_element_inorder(k, root.left)
    elif k > root.lsc + 1:
      self.find_kth_element_inorder(k, root.right)
  
