#!/usr/ruby
=begin
	Given a singly linked list, starting from the second node.	
=end

class Node
	attr_accessor :value, :next
	def initialize(value)
		@value = value
		@next = nil
	end	
end


class Singlylinkedlist
	attr_accessor :tail, :head, :next
	def initialize(value)
		@head = Node.new(value)
		@tail = @head
	end	

	def addnode(value)
		@tail.next = Node.new(value)
		@tail = @tail.next
	end
	
	def print()
		cur = @head
		while(cur != nil)
			puts cur.value
			cur = cur.next
		end
	end

end	

def del_alternate(singly)
	tail = singly.head
	while tail.next != nil
		tail.next = tail.next.next
		puts tail.value
		tail = tail.next
	end
	puts tail.value
end	

singly = Singlylinkedlist.new(1)
singly.addnode(2)
singly.addnode(3)
singly.addnode(4)
singly.addnode(5)
del_alternate(singly)