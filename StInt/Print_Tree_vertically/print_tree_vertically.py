#!/usr/bin/python

class Node(object):
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class Bsearchtree(object):
  def __init__(self):
    self.root = None
    self.vertical_count = {}

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
      elif value > root.value:
        if root.right != None:
          self.add_node(value, root.right)
        else:
          root.right = Node(value)
   
  def find_distance(self, root, count = 0)
    if root.left != None:
      self.find_distance(root.left, count - 1)
    self.vertical_distance[root.value] = count
    if root.right != None:
      self.find_distance(root.right, count + 1)   
