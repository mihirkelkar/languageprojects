"""
This version of a circular linked list is specifically modelled
to solve the Josephus problem Puzzle
"""
class Node(object):
  def __init__(self):
    self.value = None
    self.next = None
    self.prev = None

class CircLinkedList(object):
  def __init__(self, length):
    self.head = None
    self.tail = None
    self.length = length

  def buildCircle(value)
    self.head = Node(0)
    curr = self.head
    for ii in range(self.length - 1):
      temp = Node(ii + 1)
      temp.prev = curr
      curr.next = temp
      curr = curr.next
    self.tail = curr
    self.tail.next = self.head
    self.head.prev = self.tail

  def printCircle():
    curr = self.head
    

