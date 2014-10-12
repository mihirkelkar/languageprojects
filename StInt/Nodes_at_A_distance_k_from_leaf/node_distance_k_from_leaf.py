#!/usr/bin/python

class Node(object):
  def __init__(self, value):
    self.value = value
    self.next = None
    self.level = None

class BSTree(object):
  def __init__(self):
    self.root = None
  
  def add_node(self, value, level = 0, root = None):
    root = self.root if root is None else root
    if self.root == None:
      self.root = Node(value)
    if value <= root.value:
      if root.left != None:
        self.add_node(value, level + 1, root.left)
      else:
        root.left = Node(value)
    elif value > root.value:
      if root.right != None:
        self.add_node(value, level + 1, root.right)
      else:
        root.right = Node(value)

  def find_height_from_leaf(self, k, root)
    if root == None:
      return -1
    else:
      left_max = 1 + find_height_from_leaf(k, root.left)
      right_max = 1 + find_height_from_right(k, root.right)
    if left_max  + self.level == k:
      return left_max
    elif right_max + root.level == k:
      return right_max
    else:
      return max(left_max, right_max)
  

  def print_leaf_nodes(self,k, root = None):
    root = self.root if root is None else root
    height = self.find_height_from_leaf(root)
    if k == height:
      print root.value
    if root.left != None:
      self.print_leaf_nodes(k, root.left)
    if root.right != None:
      self.print_leaf_nodes(k, root.right)    
