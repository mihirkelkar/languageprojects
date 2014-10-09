class Node(object):
  def __init__(self, value):
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
      self.tail  = self.tail.next     

  def print_linkedlists(self):
    temp = self.head
    while temp != None:
      print temp.value,
      print "-->"
      temp = temp.next 


def intersection_finder(linkedlist_one, linkedlist_two):
  count_one = 0
  count_two = 0
  cur = linkedlist_one.head
  while cur != None:
    cur = cur.next
    count_one += 1
  cur = linkedlist_two.head
  while cur != None:
    cur = cur.next
    count_two += 1
  cur_one = linkedlist_one.head
  cur_two = linkedlist_two.head
  if count_one > count_two:
    for ii in range(0, (count_one - count_two)):
      cur_one = cur_one.next
  elif count_two > count_one:
    for ii in range(0, (count_two - count_one)):
      cur_two = cur_two.next
  while cur_one != None or cur_two != None:
    if cur_one != cur_two:
      cur_one = cur_one.next
      cur_two = cur_two.next
    else:
      print "Found the intersection point."
      print "The values of the intersection point is %s" %cur_one.value
      break

def main():
  LinkedOne = LinkedList()
  LinkedTwo = LinkedList()
  for ii in range(0, 5):
    LinkedOne.add_node(ii)
  for ii in range(0, 7):
    LinkedTwo.add_node(ii) 
  temp = LinkedOne.tail
  #print temp.value
  LinkedTwo.tail.next = temp
  for ii in range(99, 103):
    LinkedOne.add_node(ii) 
  LinkedOne.print_linkedlists()
  print "- - - - - - - - - - - - - - - "
  print "- - - - - - - - - - - - - - - "
  LinkedTwo.print_linkedlists()

if __name__ == "__main__":
  main()
