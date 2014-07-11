"""
The intention of this exercise is to see if the linkedlist has duplicate elements and if they do then delete them. 
We can keep a track of all the node values in the linkedlist using a hash table
"""

class Node(object):
	def __init__(self, value):
		self.value = value
		self.next = None

class LinkedList(object):
	def __init__(self):
		self.head = None
		self.tail = self.head
		self.hashtable = {}
	def add_node(self, value):
		if self.head == None:
			self.head = Node(value)
			self.tail = self.head
		else:					
			self.tail.next = Node(value)
			self.tail = self.tail.next
	def print_node(self):
		cur = self.head
		while(cur != None):
			print cur.value
			cur = cur.next		

def dedup(linkedlist):
	cur = linkedlist.head
	hashtable = {}
	while cur != None:
		try:
			temp = hashtable[cur.next.value]
			cur.next = cur.next.next
			print "Deleting node" + str(cur.next.value)
		except:
			hashtable[cur.value] = 1
		cur = cur.next
	linkedlist.print_node()			

def main():
	linked_list_one = LinkedList()
	linked_list_one.add_node(1)
	linked_list_one.add_node(2)
	linked_list_one.add_node(3)
	linked_list_one.add_node(4)
	linked_list_one.add_node(5)
	linked_list_one.add_node(1)
	linked_list_one.print_node()
	dedup(linked_list_one)
if __name__ == "__main__":
	main()					
