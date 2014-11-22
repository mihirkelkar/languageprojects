#!/usr/ruby
class Node
	attr_accessor :value, :left, :right
	def initialize(value)
		@value = value
		@left = nil
		@right = nil
	end	
end	

class Btree
	attr_accessor :root
	def initialize()
		@head = nil
	end	
    
    def insert(value)
    	add_node(value, @head)
    end	
	
	def add_node(value, cur)
    	if cur == nil
    		cur = Node.new(value)
    	else
    		if value <= cur.value
    			add_node(value, cur.left)
    		elsif value > cur.value
    			add_node(value, cur.right)
    		end		
	end	

	def depth_counter(k)
		actual_coutner(k, 0, @head)
	end	
end	