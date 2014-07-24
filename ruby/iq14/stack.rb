#!/usr/bin/ruby
class Node
	attr_accessor :value, :bottom 
	def initialize(value)
		@value = value
		@bottom = nil
	end	
end	

class Stack
	def initialize(value)
		@top = Node.new(value)
	end	

	def push(value)
		temp = Node.new(value)
		temp.bottom = @top
		@top = temp
	end	

	def pop()
		if @top != nil
			value = @top.value
			@top = @top.bottom
			return value
		else
			puts "Stack is empty can't pop"	
		end	
	end	

	def peak()
		if @top != nil
			return @top.value
		else
		 	puts "Stack is empty"	
		end	
	end

	def printStack()
		cur = @top
		while(cur != nil)
			puts "------------"
			puts cur.value
			puts "------------"
			cur = cur.bottom
		end	
	end	
end	

Stack_one = Stack.new(1)
Stack_one.printStack()
Stack_one.push(2)
Stack_one.push(3)
Stack_one.push(4)
Stack_one.push(5)
Stack_one.push(6)
Stack_one.printStack()
Stack_one.pop()
Stack_one.printStack()