#!/usr/bin/python

import math

class Max_Heap(object):
  def __init__(self):
    self.heap = [None]

  def heapify(self):
    index = len(self.heap) - 1
    while index > 1 and self.heap[index] > self.heap[int(math.floor(index / 2))]:
      print " ** %s **" %index
      temp = self.heap[int(math.floor(index / 2))]
      self.heap[int(math.floor(index / 2))] = self.heap[index]
      self.heap[index]  = temp
      index = int(math.floor(index / 2))

  def percolate_down(self):
    index = 1
    while index < len(self.heap) // 2 and self.heap[index] < max(self.heap[2 * index], self.heap[2 * index + 1]):
      if self.heap[2 * index] > self.heap[2 * index + 1]:
        temp = self.heap[2 * index]
        self.heap[2 * index] = self.heap[index]
        self.heap[index] = temp
        index = 2 * index
      else:
        temp = self.heap[2 * index + 1]
        self.heap[2 * index + 1] = self.heap[index]
        self.heap[index] = temp
        index = 2 * index + 1

  def add_node(self, value):
    self.heap.append(value)
    self.percolate_down()

  def get_max(self):
    temp = self.heap[1]
    self.heap[1] = self.heap[-1]
    self.heap = self.heap[:-1]
    self.heapify()
    return temp

  def print_heap(self):
    print self.heap
    print "============"

maxh = Max_Heap()
maxh.add_node(12)
maxh.add_node(24)
maxh.add_node(48)
maxh.add_node(2)
maxh.add_node(50)
maxh.get_max()
maxh.print_heap()
