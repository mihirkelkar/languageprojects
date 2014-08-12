"""
Implementation of a doubly linked list parent class
"""

class Node(object):
  def __init__(self, value):
    self.next = None
    self.prev = None
    self.value = value

class DoublyLinked(object):
  def __init__(self):
    self.head = None
    self.tail = None

  def addNode(self, value):
    if self.head == None:
      self.head = Node(value)
      self.tail = self.head
    else:
      curr = Node(value)
      self.tail.next = curr
      curr.prev = self.tail
      self.tail = self.tail.next

  def printList(self):
    curr = self.head
    while(curr != None):
      print "The value of the this node is %s" %curr.value
      print "------------"
      curr = curr.next      

def main():
  Doubly = DoublyLinked()
  Doubly.addNode(12)
  Doubly.addNode(23)
  Doubly.addNode(34)
  Doubly.addNode(45)
  Doubly.addNode(56)
  Doubly.printList()

if __name__ == "__main__":
  main()       
