from doubly_linked_list import DoublyLinked, Node

"""
Implemenatation of the deque datastructure using the doubly Linked list
parent class
"""

class Deque(DoublyLinked):
  def __init__(self):
    super(Deque, self).__init__()

  def addAtEnd(self, value):
    self.addNode(value)
    self.printList()

  def addAtStart(self, value):
    tempNode = Node(value)
    self.head.prev = tempNode
    tempNode.next = self.head
    self.head = tempNode
    self.printList()

  def removeAtEnd(self):
    if self.tail.prev != None:
      self.tail = self.tail.prev
      self.tail.next = None
      self.printList()
    else:
      self.tail = None
      self.head = None
      print "Its an empty Deque"
  
  def removeAtStart(self):
    if self.head.next != None:
      self.head = self.head.next
      self.head.prev = None
      self.printList()
    else:
      self.head = None
      self.tail = None
      print "Its an empty Deque"

def main():
  DoubleQ = Deque()
  DoubleQ.addAtEnd(10)
  DoubleQ.addAtStart(2)
  DoubleQ.removeAtEnd()
  DoubleQ.removeAtStart()

if __name__ == "__main__":
  main()
