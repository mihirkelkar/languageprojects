#!/usr/ruby

class Node
	attr_accessor :value, :next
	def initialize(value)
		@value = value
		@next = nil
	end	
end

class Queue
	attr_accessor :head, :tail
	def initialize()
		@head = nil
		@tail = nil
	end	

	def enqueue(value)
		if @head == nil
			@head = Node.new(value)
			@tail = @head
		else
			@tail.next = Node.new(value)
			@tail = @tail.next
		end	
	end	

	def dequeue(value)
		if @head != nil
			return nil
		else
			return @head.value
			@head = @head.next	
		end	
	end

	def printQueue()
		cur  = @head
		while cur != nil
			puts "----------"
			puts cur.value
			puts "----------"
			cur = cur.next
		end	
	end	
end

class Stack
	def initialize()
		@queue = Queue.new()
	end	

	def push(value)
		@queue.enqueue(value)
	end	

	def pop()
		cur = @queue.head
		if cur == nil 
			return nil
		elsif cur.next == nil
			temp =  cur.value
			cur = nil
			return temp
		else			
			while(cur.next.next != nil)
				cur = cur.next
			end	
			value = cur.next.value
			@queue.tail = cur
			@queue.tail.next = nil
			return value
		end	
	end	
end	

Stack_one = Stack.new()
Stack_one.push(1)
Stack_one.push(2)
puts Stack_one.pop()
puts Stack_one.pop()