class Node(object):
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class BTree(object):
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
      elif value > root.value:
        if root.right != None:
          self.add_node(value, root.right)
        else:
          root.right = Node(value)
  
  def mirror_tree(self, root):
    if root == None:
      return 
    else:
      self.mirror_tree(root.left)
      self.mirror_tree(root.right)
      temp = root.left
      root.left = root.right
      root.right = temp
