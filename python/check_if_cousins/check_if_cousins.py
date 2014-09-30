#!/usr/bin/python

#Two nodes can be called as cousins if they are on the same level and their parents are differnt

#Pass refernce to nodes, as in pass like root.left.left
def check_if_cousin(root, node1, node2):
  #Check if they are the same thing, If so return False
  if (node1 == node2) or root == None:
    return False
  else:
    #Find the level of node1 and node2
    level_one = find_level(root, node1)
    level_two = find_level(root, node2)
    if(level_one == level_two and level_one != 0):
      if !same_parent(root, node1, node2):
        return True
    return False
     

def same_parent(root, node1, node2):
  #Check if both nodes have the same parent
  if root  == None:
    return False
  return (root.left == node1 and root.right == node2 || root.right == node1 and root.left == node2 || same_parent(root.left, node1, node2) || same_parent(root.right, node1, node2))
           

#IMP find level / search function in a normal binary tree
def find_level(root, node1, count):    
  if root == None:
    return 0
  if root == node1:
    return count
  #Check if its present in the left subtree. 
  level = find_level(root.left, node1, count + 1)
  if(level != 0):
    return level
  return find_level(root.right, node1, count + 1)
