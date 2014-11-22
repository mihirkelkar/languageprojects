#!/usr/bin/python

class Node(object):
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList(object):
  def __init__(self):
    self.head = None
    self.tail = None
    self.count = 0
  
  def add_node(self, value):
    if self.head == None:
      self.head = Node(value)
      self.tail = self.head
      self.count += 1
    else:
      self.tail.next = Node(value)
      self.tail  = self.tail.next
      self.count -= 1

  def del_kth_from_last(self, k):
    if k > self.count:
      print "Not possible"
    else:
      cur = self.head
      for ii in range(0, k):
        cur = cur.next
    tracker = self.head
    while cur.next != None:
      cur = cur.next
      tracker = tracker.next
      
