class Node(object):
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList(object):
  def __init__(self, value):
    self.head = None
    self.tail = None
  
  def add_node(self, value):
    if self.head == None:
      self.head = Node(value)
      self.tail = self.head
    else:
      self.tail.next = Node(value)
  
  def reverse_k_nodes(k, bool, head = None):
    if head == None:
      return 

    if bool:
      cur = head
      while k > 0 and cur != None:
        temp = cur
        cur = cur.next
        cur.next = temp
      head.next = reverse_k_nodes(k, False, cur)
    else:
      cur = head
      while k > 0 and cur != None:
        cur = cur.next
      head.next = reverse_k_nodes(k, True, cur)
     return head  
