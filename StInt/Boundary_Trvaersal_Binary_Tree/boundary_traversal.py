#!/usr/bin/python

#Assume all of these are class methods of the class BSTree. 

def printLeaves(self, root):
  if root != None:
    self.printLeaves(root.left)
    if root.left == None and root.right == None:
      print root.data
    self.printLeaves(root.right)

#Go ahead and trace the left boundary
def printBoundaryLeft(self, root):
  if root != None:
    if root.left != None:
      print root.data
      self.printBoundaryLeft(root.left)
    elif root.right != None:
      print root.data
      self.printBoundaryLeft(root.right)

def printBoundaryRight(self, root):
  if root != None:
    if root.right != None:
      print root.data
      self.printBoundaryRight(root.right)
    elif root.left != None:
      print root.data
      self.printBoundaryRight(root.left)

def boundaryTraversal(self, root):
  if root != None:
    print root.data
    self.printBoundaryLeft(root.left)
    self.printLeaves(root.left)
    self.printLeaves(root.right)
    self.printBoundaryRight(root.right)
  

