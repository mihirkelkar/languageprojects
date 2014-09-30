class Node(object):
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class BinaryTree(object):
  def __init__(self):
    self.head = None
  #Function to insert nodes into a binary tree (Not a BST)
  def insert(self, value, root = None):
    root = self.root if root is None else root
    if root.left == None:
      root.left = Node(value)
    else:
      queue = [self.root]
      while queue:
        temp = queue.pop(0)
        if temp.left == None:
          temp.left = Node(value)
          break
        elif temp.right == None:
          temp.right = Node(value)
          break
        elif temp.left != None and temp.right != None:
          queue.append(temp.left)
          queue.append(temp.right)

  def print_tree(self, root = self.root):
        if root != None:
          print root.value
          if root.left != None:
            self.print_tree(root.left)
          if root.right != None:
            self.print_tree(root.right)










