#Implement a Queue using Stack. 
from stack import *

class myQueue(object):
  def __init__(self):
    self.first_stack = Stack()
    self.second_stack = Stack()

  def enqueue(self, value):
    if self.first_stack.top == None:
      while(self.second_stack.top != None):
        self.first_stack.push(self.second_stack.pop())
    self.first_stack.push(value)

  def dequeue(self):
    while self.first_stack.top != None:
      self.second_stack.push(self.first_stack.pop())
    return self.second_stack.pop()

  def printQueue(self):
    while self.first_stack.top != None:
      self.second_stack.push(self.first_stack.pop())
    current = self.second_stack.top
    while current != None:
      print current.value
      current = current.bottom
    print " - - - - - - - "

def main():
  mQ = myQueue()
  mQ.enqueue(1)
  mQ.enqueue(2)
  mQ.enqueue(3)
  mQ.printQueue()
  mQ.dequeue()
  mQ.enqueue(10)
  mQ.printQueue()
  mQ.dequeue()
  mQ.dequeue()
  mQ.printQueue()

if __name__ == "__main__":
  main()      
