#Design a Stack such that it has an operation called min along with push and pop which returns the min element in 0(1) time. 

#The basic idea would be to modify the  Node object such that it can hold the minimum element below it in itself. So, when something is popped out, we can reset the min immediately. 

#Another approach is to maintain a new stack of min elements. this might eb more space conservative since a lot of elements will have the same min below them. 

#i'l impleent both techniques here. The seccond alternative will be called two_stack_min.py
from stack import *

#Overriding the Node class constructor here
class Node_Min(Node):
  def __init__(self, value, min = None):
    super(Node_Min, self).__init__(value)
    self.min = min

#Overriding the class constructir for the Stack class
class Stack_Min(Stack):
  def __init__(self):
    super(Stack_Min, self).__init__()
    self.min = float("inf")
  def push(self, value):
    if self.top == Node_Min(value, value):
      self.min = self.top.value
    else:
      if value < self.min:
        self.min = value
      temp = Node_Min(value, self.min)
      temp.bottom = self.top
      self.top = temp
  def el_min(self):
    if self.top != None:
      print self.top.min

  def pop(self):
    if self.top == None:
      return None
    else: 
      temp = self.top.value
      self.top = self.top.bottom
      if temp == self.min:
        self.min = self.top.value
      return temp  

def main():
  minStack = Stack_Min()
  minStack.push(1)
  minStack.push(2)
  minStack.push(3)
  minStack.push(4)
  minStack.el_min()
  minStack.pop()
  minStack.push(0)
  minStack.el_min()

if __name__ == "__main__":
  main()
