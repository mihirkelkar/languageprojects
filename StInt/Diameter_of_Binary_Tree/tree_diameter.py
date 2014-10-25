#!/usr/bin/python

class Node(object):
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class Tree(object):
  def __init__(self):
    self.root = None
    self.max_path = 0

  def add_node(self, value, root):
    root = self.root if root is None else root
    if self.root == None:
      self.root = Node(value)
    else:
      if value <= root.value:
        if root.left != None:
          self.add_node(self, root.left)
        else:
          root.left = Node(value)
      elif value > root.value:
        if root.right != None:
          self.add_node(self, root.right)
        else:
          root.right = Node(value)

  def find_height(self,root):
    if root == None:
      return -1
    else:
      left = 1 + self.find_height(root.left)
      right = 1 + self.find_height(root.right)
      if self.max_path < left + right + 1:
        self.max_path = left + right - 1
      return max(left, right)


def find_diameter(Tree):
  Tree.find_height(Tree.root)
  print Tree.max_path

