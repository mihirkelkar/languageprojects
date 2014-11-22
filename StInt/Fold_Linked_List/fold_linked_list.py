class Node(object):
  def __init__(self,value):
    self.value = value
    self.next = None

class LinkedList(object):
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

  def reverse_linked_list(self, node):
    prev = None
    while node != null:
      nextnode = node.next
      node.next = prev
      prev = node
      node = nextnode
    node = prev
    return node

  def print_linked_list(self, head):
    while head != None:
      print head.value
      head = head.next

  def fold_linked_list(self, head_one, head_two):
    #The approach that we can use in this case is basically just go ahead and 
    #find the middle element first using the 2 pointer approach. 
    #Once that is done , we separate the second part of the list and reverse it. 

    slow = None
    fast = None
    slow = self.head
    fast = self.head
    while fast != None:
      slow = slow.next
      fast = fast.next
      if fast != Null:
        fast = fast.next
    middle = slow
    reverse_node = self.reverse_linked_list(middle)
    #Makr the element previos to middle None
    node = self.head
    while node.next != middle:
     node = node.next
    node.next = None

