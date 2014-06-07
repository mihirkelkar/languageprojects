#!/usr/bin/python
class node:
	def __init__(self, value):
		self.value =  value
		self.next = None

class linked_list:
	def __init__(self):
		self.head = None
		self.tail = None
		self.tail = self.head
	
	def addnode(self, value):
		if self.tail == None:
			self.head = node(value)
			self.tail = self.head
		else:
			self.tail.next = node(value)
			self.tail = self.tail.next
	def printlist(self):
		cur = self.head
		while(cur != None):
			print cur.value,
			print "->",
			cur = cur.next

		
def do_math(llist):
	odd_list = linked_list()
	odd = []
	even_list = linked_list()
	cur = llist.head
	cur_two = llist.head.next
	while(cur != None):
		even_list.addnode(cur.value)
		if cur.next != None:
			cur = cur.next.next
		else:
			break



	while(cur_two != None):
		odd.append(cur_two.value)
		if cur_two.next != None:
			cur_two = cur_two.next.next
	odd = odd[::-1]
	for i in odd:
		odd_list.addnode(i)
	even_list.tail.next = odd_list.head	
	even_list.printlist()
		





def main():
	ll = linked_list()
	ll.addnode(1)
	ll.addnode(2)
	ll.addnode(3)
	ll.addnode(4)
	ll.addnode(5)
	#ll.printlist()
	do_math(ll)





if __name__ == "__main__":
	main()
		
