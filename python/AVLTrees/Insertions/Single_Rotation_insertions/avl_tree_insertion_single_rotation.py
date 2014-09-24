class Node(object):
  def __init__(self, value):
    #Assuming that the entered value is an int
    self.value = value
    self.left = None
    self.right = None

class AVL_Tree(object):
  def __init__(self):
    self.root = None

  def find_height(self, root):
    if root == None:
      return -1
    else:
      return 1 + max(self.find_height(root.left), self.find_height(root.right))
  
  def find_height_difference(self, root):
    left_height = self.find_height(root.left)
    right_height = self.find_height(root.right)
    return abs(left_height - right_height)
  
  def insert(self, value, route_trace = [], root = None):
    root = self.root if root is None else root
    #print route_trace
    if root == None:
      self.root = Node(value)
    elif value <= root.value:
      route_trace.append('left')
      if root.left != None:
        route_trace = self.insert(value, route_trace, root.left)
      else:
        root.left = Node(value)
        #Maybe check for height differnce right here. This code is fucking up. 
    else:
      route_trace.append('right')
      if root.right != None:
        route_trace = self.insert(value, route_trace, root.right)
      else:
        root.right = Node(value)
    return route_trace 

def main():
  avl_tree = AVL_Tree()  
  print avl_tree.insert(5, [])
  print avl_tree.find_height(avl_tree.root)
  print "****************"
  print avl_tree.insert(2, [])
  print avl_tree.find_height(avl_tree.root)    
  print "****************"
  print avl_tree.insert(10, [])
  print avl_tree.find_height(avl_tree.root)
  print "****************"
  print avl_tree.insert(8, [])
  print avl_tree.find_height(avl_tree.root)
  print "****************"  
  print avl_tree.insert(0, [])
  print avl_tree.find_height(avl_tree.root)
  print "****************"
  print avl_tree.insert(4, [])
  print avl_tree.find_height(avl_tree.root)
  print "****************"
  print avl_tree.insert(3, [])
  print avl_tree.find_height(avl_tree.root)
  print "****************"
  print "=================================="
  print avl_tree.find_height_difference(avl_tree.root)
  print "=================================="

if __name__ == "__main__":
  main()
