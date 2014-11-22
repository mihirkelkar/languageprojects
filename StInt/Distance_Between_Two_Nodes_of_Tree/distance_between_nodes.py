#!/usr/bin/python

class Node(object):
  def __init__(self, value):
    self.value = value
    self.next = None
  
class BinaryTree(object):
  def __init__(self):
    self.root = None

  def add_node(self, value, root = None):
    root = self.root if root is None else root
    if self.root == None:
      self.root = Node(value)
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

  def find_lca(self, value1, value2, root = None):
    root = self.root if root is None else root
    if value1 < root.value and value2 < root.value:
      if root.left != None:
        lca = self.find_lca(value1, value2, root.left)
    elif value1 > root.value and value2 > root.value:
      if root.right != None:
        lca = self.find_lca(value1, value2, root.right)
    else:
      lca = root.value
    return lca

  def find_level
