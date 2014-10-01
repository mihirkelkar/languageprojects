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
      self.tail = self.tail.next

class Stack(object):
  def __init__(self):
    self.stack = list()
  def push(self, node):
    self.stack.append(node)
  def pop(self):
    print "Length of the given stack is %s" %len(self.stack)
    return self.stack.pop()

def main():
  linkedlist = LinkedList()
  linkedlist.add_node(1)
  linkedlist.add_node(2) 
  linkedlist.add_node(3)
  linkedlist.add_node(4) 
  linkedlist.add_node(3)
  linkedlist.add_node(2)
  linkedlist.add_node(1)
  stack = Stack()
  cur = linkedlist.head
  while cur != None:
    stack.push(cur)
    cur = cur.next
  cur = linkedlist.head
  while cur != None:
    temp = stack.pop()
    print temp.value
    print cur.value
    print "- - - - - - - -"
    if temp.value == cur.value:
      cur = cur.next
    else:
      print "Not a palindrome"
      return 0
  print "This is a palindrome"
  return 1    

if __name__ == "__main__":
  main()
