#!/usr/ruby

class Node
	attr_accessor :value, :left, :right
	def initialize(value)
		@value = value
		@left = nil
		@right = nil
	end	
end

class BinarySearchTree
	attr_accessor :head, :inorderlist
	def initialize()
		@head = nil 
		@inorderlist = []  
	end	

	def add_node(value, cur = nil)
		if @head == nil
			@head = Node.new(value)
		else
			if value <= cur.value
				if cur.left != nil
				  add_node(value, cur.left)
				 else
				   cur.left = Node.new(value)
				 end   	
			elsif value > cur.value
				if cur.right != nil
				  add_node(value, cur.right)
				 else
				  cur.right = Node.new(value)
				 end 	  
			end
		end					
	end		

	def inorder_traversal()
		inorder(@head)
		return @inorderlist
	end
	
	def inorder(cur)
		if cur.left != nil
			inorder(cur.left)
		end	
		@inorderlist << cur.value
		if cur.right != nil
			inorder(cur.right)
		end			
	end	 
end


def merge_bst(Tree_one, Tree_two)
  listone = Tree_one.inorder_traversal()
  listtwo = Tree_two.inorder_traversal()
  #Merge these two lists and then build a binary tree from the middle. Pretty much it

end	
Tree_one = BinarySearchTree.new()
Tree_one.add_node(5, Tree_one.head)
Tree_one.add_node(1, Tree_one.head)
Tree_one.add_node(6, Tree_one.head)
list_one = Tree_one.inorder_traversal()
puts Tree_one.inorderlist