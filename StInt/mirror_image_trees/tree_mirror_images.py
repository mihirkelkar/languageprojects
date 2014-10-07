class Node(obejct):
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class BsTree(object):
  def __init__(self):
    self.root = None
    self.traversal_list = list()
  
  def addNode(self, value, root = None):
    root = self.root if root is None else root
    if value <= root.value:
      if root.left != None:
        self.addNode(value, root.left)
      else:
        root.left = Node(value)
    else:
      if root.right != None:
        self.addNode(value, root.right)
      else:
        root.right = Node(value)
  def inorder_traversal(self, root = None):
    root = self.root if root is None else root
    if self.root == None:
      return 
    if root.left != None:
      self.inorder_traversal(root.left)
    self.traversal_list.append(root.value)
    if root.right != None:
      self.inorder_traversal(root.right)
         

def main():
  #Checking if the two trees are mirror images is to check if their 
  #inorder traversals are mirror images of one another
  tree1 = BSTree()
  tree2 = BSTree()
  if tree1.traversal_list == tree2.traversal_list[::-1]:
    return True
  else:
    return False

if __name__ == "__main__":
  main()
