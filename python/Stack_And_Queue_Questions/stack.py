#!/usr/bin/python

class Node(object):
  def __init__(self, value):
    self.value = value
    self.bottom = None

class Stack(object):
  def __init__(self):
    self.top = None
  def push(self, value):
    if self.top == None:
      self.top = Node(value)
    else:
      temp = Node(value)
      temp.bottom = self.top
      self.top = temp
  def pop(self):
    if self.top == None:
      return None
    else:
      temp = self.top.value
      self.top = self.top.bottom
      return temp

  def printStack(self):
    current = self.top
    while(current != None):
      print "| %s |" %current.value 
      print "------"
      current = current.bottom
    print " - - - - - - - - - - - - - "  
  
def main():
  testStack  = Stack()
  testStack.push(2)
  testStack.push(4)
  testStack.push(7)
  testStack.printStack()
  testStack.pop()
  testStack.printStack()
if __name__ == "__main__":
  main()     
