Transform a BST to a greater sum tree. 

By leveraging the fact that the tree is a BST, we can find a solution in O(n)
time. The idea is to traverse the tree in reverse inorder. Reverse inorder traversal of a BST gives us keys in decreasing order. Before visiting a node, we will visit all greater nodes of that tree. 

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
          root.right  = Node(value)
  
  def covert_to_greater_sum(self, value = 0, root = None):
    root = self.root if root is None else root
    if root == None:
      return
    self.convert_to_greater_sum(value, root.right)
    value = value + root.value
    root.value = value - root.value
    self.convert_to_greater_sum(value, root.left)  
