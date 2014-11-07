class Node(object):
  def __init__(self, value):
    self.value = value
    self.next = None

class Linkedlist(object):
  def __init__(self):
    self.head = None
    self.tail = None
    self.count = 0
  
  def add_node(self, value):
    if self.head == None:
      self.head = Node(value)
      self.tail = self.head
    else:
      self.tail.next = Node(value)
      self.tail  = self.tail.next
    self.count += 1

  def right_shift(self, k):
    if k >= self.count:
      print "Not enough nodes to right shift by that amount"
      return
    new_tail = None
    new_head = None
    #Adjusting both pointers
    diff = k + 1
    new_tail = self.head
    end = self.head
    while diff > 0:
      end = end.next
      diff -= 1 
    while end.next != None:
      end = end.next
      new_tail = new_tail.next

    end.next = self.head
    self.head = new_tail.next
    new_tail.next = None
    self.tail = new_tail

  def print_linkedlist(self):
    cur = self.head
    while cur != None:
      print cur.value, 
      print "-----"
      cur = cur.next
def main():
  list_one = Linkedlist()
  list_one.add_node(1)
  list_one.add_node(2) 
  list_one.add_node(3)
  list_one.add_node(4)
  list_one.print_linkedlist() 
  list_one.right_shift(2)
  print '= = = = = = = = = = =\n= = = = = = = = = = '
  list_one.print_linkedlist()
if __name__ == "__main__":
  main()
