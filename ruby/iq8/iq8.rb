#!/usr/ruby

class Node
	attr_accessor :value, :next
	def initialize(value)
		@value = value
		@next = nil
	end
end

class Linkedlist
	def initialize()
		@head = nil
		@tail = nil
	end
	
	def addnode(value)
		if @tail == nil
			@head = Node.new(value)
			@tail = @head
		else
			@tail.next = Node.new(value)	
			@tail = @tail.next
		end

	end

end
