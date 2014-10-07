#!/usr/bin/python

class Node(object):
  def __init__(self, data):
    self.value = data
    self.left = None
    self.right = None

class BSTree(object):
  def __init__(self):
    self.root = None
    self.pre_order_list = list()
  
  def add_node(self, value, root  = None):
    root = self.root if root is None else root
    if self.root == None:
      self.root = Node(value)
    elif value <= root.value:
      if root.left != None:
        self.add_node(value, root.left)
      else:
        root.left = Node(value)
    else:
      if root.right != None:
        self.add_node(value, root.right)
      else:
        root.right = Node(value)
  
  def pre_order(self, root = None):
    root  = self.root if root is None else root
    self.pre_order_list.append(root.value)
    if root.left != None:
      self.pre_order(root.left)
    if root.right != None:
      self.pre_order(root.right)


def main():
  Tree_one = BSTree()
  Tree_one.add_node(10)
  Tree_one.add_node(5)
  Tree_one.add_node(12)
  Tree_one.add_node(11)
  Tree_one.pre_order()
  print Tree_one.pre_order_list
  Tree_two = BSTree()
  for ii in Tree_one.pre_order_list:
    Tree_two.add_node(ii)
  Tree_two.pre_order()
  print Tree_two.pre_order_list 
if __name__ == "__main__":
  main()


