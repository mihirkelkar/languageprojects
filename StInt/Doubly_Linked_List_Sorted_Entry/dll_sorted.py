import random

class Node(object):
  def __init__(self, value):
    self.value = value
    self.prev = None
    self.next = None

class Doubly_Linked_List(object):
  def __init__(self):
    self.head = None
    self.tail = None

  def insert_sorted(self, value):
    if self.head == None:
      self.head = Node(value)
      self.tail = self.head
    else:
      if value >= self.tail.value:
        self.tail.next = Node(value)
        prev = self.tail
        self.tail = self.tail.next
        self.tail.prev = prev
      else:
        previous = None
        current = self.head
        while(current.next != None and current.value < value):
          previous = current
          current = current.next
        if previous == None:
          temp = Node(value)
          temp.next = self.head
          self.head.prev = temp
          self.head = temp
        else:
          previous.next = Node(value)
          previous.next.next = current
          previous.next.prev = previous

  def lprint(self):
    current = self.head
    while(current != None):
      print current.value,
      print "-->",
      current = current.next
    print "|"


def main():
  dll = Doubly_Linked_List()
  for ii in range(0, 10):
    dll.insert_sorted(random.randint(-100, 100))
  dll.lprint()
if __name__ == "__main__":
  main()
