#!/usr/bin/python

class Node(object):
  def __init__(self, value):
    self.bottom = None
    self.next = None
    self.value = value

class GridUsingLList(Node):
  def __init__(self, height, length):
    self.prev = None
    self.top = None 
    self.left = None
    self.height = height
    self.length = length

  def make_grid(self):
    for ii in range(self.height):
      self.left = Node(None)
      cur = self.left
      for jj in range(self.length - 1):
        temp = Node(None)
        cur.next = temp
        cur = temp
      if ii == 0:
        self.top = self.left
        self.prev = self.left
      elif ii != 0:
        cur = self.prev
        curr = self.left
        while cur != None:
          cur.bottom = curr
          cur = cur.next
          curr = curr.next
        self.prev = self.left

  def add_value(self, x, y, value):
    if (x > self.length or x < 0) or (y > self.height or y < 0):
      print "Cant go beyond the dimensions"
    else:
      cur = self.top
      for ii in range(x):
        cur = cur.next
      for jj in range(y):
        cur = cur.bottom 
      cur.value = value

  def print_grid(self):
    cur = self.top
    for ii in range(self.height):
      next = cur.bottom
      for jj in range(self.length):
        print cur.value,
        cur = cur.next
      print "\n"
      print "-" * 40
      cur = next
            

def main():
  grid = GridUsingLList(10,10)
  grid.make_grid()
  grid.add_value(2,2,2)
  grid.add_value(4,2,2)
  grid.print_grid()

if __name__ == "__main__":
  main()
