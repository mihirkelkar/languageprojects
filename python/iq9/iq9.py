class node:
  def __init__(self, value):
    self.prev = None
    self.next = None
    self.child = None
    self.value = value

  def addchild(self, value):
    self.child = node(value) 


class multleveldll:
  def __init__(self):
    self.head = None
    self.tail = None

  def addnode(self, value, cur = None):
    cur = self.tail if cur is None else cur
    if cur == None:
      self.head = node(value)
      self.tail = self.head
    elif cur != None:
      if cur == self.tail:
        self.tail.next = node(value)
        self.tail.next.prev = self.tail
        self.tail = self.tail.next
      elif cur != self.tail:
        cur.next = node(value)
        cur.next.prev = cur       

  def printlist(self, cur = None):
    cur = self.head if cur is None else cur
    while cur != None:
      print cur.value   
      if cur.child != None:
        print "++++++++++"
        self.printlist(cur.child)
	print "++++++++++"
      cur = cur.next

  def flatten(self, cur = None):
    #print "In flatten"
    cur = self.head if cur is None else cur
    while(cur != None):
      #print "Inside the loop"
      if cur.child != None:
	temp = cur.next
        #print temp.value
        if cur.child.next != None:
          tmpr = cur.child.next
          while tmpr.next != None:
            tmpr = tmpr.next
        else:
          tmpr = cur.child
        tmpr.next = temp
        temp.prev = tmpr
        cur.next = cur.child
        cur.child = None
      #print cur.value
      cur = cur.next 
      #print cur.value
      
def main():
  listone = multleveldll()
  listone.addnode(5)		
  listone.head.addchild(6)
  listone.addnode(25, listone.tail.child)
  listone.tail.child.next.addchild(8)
  listone.addnode(6, listone.tail.child.next)
  listone.tail.child.next.next.addchild(9)
  listone.tail.child.next.next.child.addchild(7)
  listone.addnode(33)
  listone.addnode(17)
  listone.addnode(2)
  listone.tail.addchild(2)
  listone.addnode(7, listone.tail.child)
  listone.tail.child.addchild(12)
  listone.addnode(5, listone.tail.child.child)
  listone.tail.child.child.addchild(21)
  listone.addnode(3, listone.tail.child.child.child)
  listone.addnode(1)
  listone.printlist()
  listone.flatten()
  print "------------"
  listone.printlist()
if __name__ == "__main__":
  main()
