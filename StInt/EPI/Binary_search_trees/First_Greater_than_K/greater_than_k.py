class Node(object):
  def __init__(self, value):
    self.value = value
    self.left = None 
    self.right = None
    self.parent = None
  
class BSTree(object):
  def __init__(self):
    self.root = None
  
  def add_node(self, value, root = None) :
    root = self.root if root is None else root
    if self.root == None:
      self.root = Node(value)
    else:
      if value <= root.value:
        if root.left != None:
          self.add_node(value, root.left)
        else:
          root.left = Node(value)
          root.left.parent = root
      elif value > root.value:
        if root.right != None:
          self.add_node(value, root.right)
        else:
          root.right = Node(value)
          root.right.parent = root


def find_greater_than_k(root, k):
  if k < root.value:
    find_greater_than_k(root.left, k)
  elif k > root.value:
    find_greater_than_k(root.right, k)
  elif root.value == k:
    if root.right != None:
      root = root.right
      while(root.left != None):
        root = root.left
      return root.value  
    elif root.right == None:
      while root == root.parent.right:
        root = root.parent
      return root.parent.value        
      

