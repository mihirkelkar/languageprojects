#!/usr/bin/python

#Deleting duplicates nodes from a sorted linked list

class ListNode(object):
  def __init__(self, value):
    self.value = value
    self.next = None
    
class LinkedList(object):
  def __init__(self):
    self.head = None
    self.tail = None
  
  def add_node(self, value):
    if self.head == None:
      self.head = ListNode(value)
      self.tail = self.head
    else:
      self.tail.next = ListNode(value)
      self.tail = self.tail.next

  def print_nodes(self):
    node = self.head
    while node != None:
      print node.value,
      print "->",
      node = node.next
  
def delete_duplicates_from_sorted(linkedlist):
  node = linkedlist.head
  while node.next != None:
    if node.value != node.next.value:
      node = node.next
    else:
      node.next = node.next.next
  return linkedlist

def main():
  Ll = LinkedList()
  Ll.add_node(1)
  Ll.add_node(1)
  Ll.add_node(1)
  Ll.add_node(2)
  Ll.add_node(2)
  Ll.add_node(2)
  Ll.add_node(3)
  Ll.add_node(3)
  Ll.print_nodes()
  print "=========="
  delete_duplicates_from_sorted(Ll).print_nodes()
  print "=========="

if __name__ == "__main__":
  main()
