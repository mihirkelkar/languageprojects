#Implementing an alternative method to retrieve the element which is the minium amongst a given set. 
from stack import *

class Stack_Min(object):
  def __init__(self, stack):
    self.top = None
    self.min_stack = stack
    self.minval = float("inf")

  def push(self, value):
    if self.top == None:
      self.top = Node(value)
    else:
      temp = Node(value)
      temp.bottom = self.top
      self.top = temp
    if self.minval > value:
      self.minval = value
      self.min_stack.push(value)

  def pop(self):
    if self.top == None:
      return None
    else:
      temp = self.top.value
      self.top = self.top.bottom
      if temp == self.min_stack.top.value:
        self.min_stack.pop()
      return temp 

  def getMin(self):
    return self.min_stack.top.value

  def printMinStack(self):
    current = self.top
    while(current != None):
      print "| %s |" %current.value
      print "------"
      current = current.bottom
    print "- - - - - - - - -"

def main():
  minStack = Stack()
  testStack = Stack_Min(minStack)
  testStack.push(1)
  testStack.push(2)
  testStack.push(0)
  #testStack.push(7)
  #testStack.printMinStack()
  #testStack.min_stack.printStack()
  print testStack.getMin()
  testStack.pop()
  print testStack.getMin()

if __name__ == "__main__":
  main()

