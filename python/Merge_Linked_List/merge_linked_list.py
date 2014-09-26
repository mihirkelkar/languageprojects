#!/usr/bin/python

import random

class Node(object):
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList(object):
  def __init__(self):
    self.head = None
    self.tail = None

  def insert_node(self, value):
    if self.head == None:
      self.head = Node(value)
      self.tail = self.head
    else:
      self.tail.next = Node(value)

def merge_linked_lists(node1, node2):
  if node1 == None:
    return node2
  if node2 == None:
    return node1
  if node1.value <= node2.value:
    node1.next = merge_linked_lists(node1.next, node2)
    return node1
  else:
    node2.next = merge_linked_lists(node2.next, node1)
    return node2

def main():
  linked_list_one = LinkedList()
  linked_list_two = LinkedList()
  for ii in range(1, 10):
    linked_list_one.insert_node(random.randint(1, 1000))
    linked_list_two.insert_node(random.randint(1, 1000))
  node_one = merge_linked_lists(linked_list_one.head, linked_list_two.head)

if __name__ == "__main__":
  main()
