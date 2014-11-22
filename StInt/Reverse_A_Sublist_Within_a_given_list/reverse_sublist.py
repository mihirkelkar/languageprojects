class Node(object):
  def __init__(self, value):
    self.value = value
    self.next = None
  
class Linkedlist(object):
  def __init__(self):
    self.head = None
    self.tail = None
  
  def add_node(self, value):
    if self.head == None:
      self.head = Node(value)
      self.tail = self.head
    else:
      self.tail.next = Node(value)
      self.tail = self.tail.next
  
  def reverse_sublist(self, start, end):
    diff = end - start
    current = self.head
    while start > 1:
      current = current.next
      start -= 1
    if current.next != None:
      temp = current.next
      prev = current
      while diff >= 0:
        next = temp.next
        temp.next = prev
        prev = temp
        temp = next
        diff -= 1
     current.next = prev
     node = current
     
     
