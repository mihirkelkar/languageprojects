"""
This code illustrates an implementation of a priority queue using the 
sorted linked list class that I wrote previously
80 character limit indicator below
-------------------------------------------------------------------------------
"""

class Node(object):
  def __init__(self, value):
    try:
      self.value = int(value)
    except:
      print "Value has to be an integer"
    self.next = None

class Linkedlist(object):
  def __init__(self):
    self.head = None
    self.tail = None
  
  def addNode(self, value):
    if self.head == None:
      self.head = Node(value)
      self.tail = self.head
    elif self.head != None:
      #For a value >= tail value, add to the end of the linked list
      if value >= self.tail.value:
        self.tail.next = Node(value)
        self.tail = self.tail.next
      elif value <= self.head.value:
      #For a value <= the head value, add ot the head of the list.
        curr = Node(value)
        curr.next = self.head
        self.head = curr
      elif value > self.head.value and value < self.tail.value:
        currNode = Node(value)
        cur = self.head
        while(cur != None):
          if cur.next.value >= value:
 	    currNode.next = cur.next
            cur.next = currNode
            break
          else:
            cur = cur.next
  
  def printList(self):
    print "-----------------"
    cur = self.head
    while(cur != None):
      print "The value for this node is %s" %cur.value
      print "****"
      cur = cur.next

class PriorityQueue(Linkedlist):
  def __init__(self):
    super(PriorityQueue, self).__init__()
  def enqueue(self, value):
    self.addNode(value)
    self.printList()
  def dequeue(self):
    value = self.head
    self.head = self.head.next
    self.printList()
    return value

def main():
  Priorityqueue = PriorityQueue()
  Priorityqueue.enqueue(23)
  Priorityqueue.enqueue(12)
  Priorityqueue.dequeue()
if __name__ == "__main__":
  main()
