import random


class Node(object): 
  def __init__(self, value): 
    self.value = value
    self.left = None
    self.right = None
 
  def insert(self, value): 
    if self.value == None: 
      self.value = value
    else: 
      if value <= self.value and self.left != None: 
        self.left.insert(value) 
        return 
      elif value <= self.value and self.left == None: 
        self.left = Node(value)
        return  
      elif value > self.value and self.right != None: 
        self.right.insert(value)
        return 
      elif value > self.value and self.right == None :
        self.right = Node(value)
        return 

  def traverse(self, node, max_reached=False): 
    if self.right == None and self.left == None: 
      return True
    
    if self.right != None: 
      max_reached = self.traverse(self.right)
      if max_reached: 
        print(self.value) 
    
    if self.right == None and self.left != None: 
      if max_reached: 
        print(self.value)
      self.traverse(self.left, max_reached=True)

    if self.right != None and self.left != None: 
      self.traverse(self.left)

     

class BST(object): 
  def __init__(self): 
    self.root = None

  def insert(self, value): 
    if self.root == None: 
      self.root = Node(value)
    else: 
      self.root.insert(value)

  def right_left_root_traversal()
    cur_node = self.root
    if cur_node.right != None: 
      cur_node

def find_second_largest_node(tree): 
  if tree.root == None: 
    return None
  elif tree.root.left == None and tree.root.right == None: 
    return tree.root.value
  else: 
    tree.right_left_root_traversal()


def main(): 
  tree = BST()
  for ii in range(0, 100): 
    tree.insert(random.randint(1, 10000))
  
  print(tree.root.value)
  print(tree.root.left.value)
  print(tree.root.right.value)

main()
    
