#!/usr/bin/python

class Node(object):
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class BSTree(object):
  def __init__(self):
    self.root = None
    self.max_sum_so_far = 0

  def add_node(self, value, root = None):
    root = self.root if root is None else root
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

  def find_max_sum(self, root = None):
    root = self.root if root is None else root
    if root == None:
      return 0
    left_val = self.find_max_sum(root.left)
    right_val = self.find_max_sum(root.right)
    if root.data + left_val + right_val > self.max_sum_so_far:
      self.max_sum_so_far = root.data + left_val + right_val
    return 
      root.data + max(left_val, right_val)



