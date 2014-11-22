class Node(object):
  def __init__(self, value):
    self.value = value
    self.next = None

class Cycle_Linked_list(object):
  def __init__(self):
    self.head == None:
    self.tail == None:
  
  def insert_element(self, value):
    if self.head == None:
      self.head == Node(value)
      self.head.next = self.head
    elif value <= self.head.value:
     #if max or min, add to the head of the queue
    else:
      current = self.head
      prev = None:
      while value >= current.value:
        prev = current
        current = current.next
      prev.next = Node(value)
      prev.next.next = current
      
      
        
