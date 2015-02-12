class Node(object):
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

in_order_list = [-float("inf")] 
def check_if_BST(root): 
  leftval, rightval = True, True 
  if root.left != None:
    leftval = check_if_BST(root.left)
  in_order_list.append(root.value)
  if root.value <= in_order_list.pop(0):
    return False
  if root.right != None:
    rightval = check_if_BST(root.right)
  return leftval and rightval

rootbst = Node(5)
rootbst.left = Node(4)
rootbst.right = Node(6)
rootbst.left.left = Node(2) 

notbst = Node(1)
notbst.left = Node(2)
notbst.right = Node(3)

print check_if_BST(rootbst)  
print check_if_BST(notbst)  
