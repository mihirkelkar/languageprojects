class Node(object):
  def __init__(self, value):
    self.value = value
    self.next = None


def remove_duplicates(head):
  current = head
  while current.next != None:
    if current.value != current.next.value:
      current = current.next
    elif current.value == current.next.value:
      temp = current.next
      while temp != None and temp.value == current.value:
        temp = temp.next
      current.next = temp

def print_node(head):
  current = head
  while current != None:
    print current.value
    current = current.next
  
def main():
  a = Node(1)
  b = Node(2)
  c = Node(3) 
  d = Node(4)
  e = Node(5)
  f = Node(6)
  g = Node(6)
  a.next = b
  b.next = c
  c.next = d
  d.next = e
  e.next = f
  f.next = g
  print_node(a)
  remove_duplicates(a)
  print_node(a)

if __name__ == "__main__":
  main()

  
       
