#!/usr/bin/python

class Node(object):
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
  
class BSTree(object):
  def __init__(self):
    self.root = None
  
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
  
  def check_if_balanced(self, root):
    if root == None:
      return -1, True
    else:
      left_val = self.check_if_balanced(root.left)
      right_val = self.check_if_balanced(root.right)
      if left_val[1] and right_val[1]:
        return max(left_val[0], right_val[1])
      return False 
        
        
