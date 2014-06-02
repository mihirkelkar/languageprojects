#!/usr/ruby

class Node
	attr_accessor :value, :left, :right
	def initialize(value)
		@value = value		
		@left = nil
		@right = nil
	end
end


class Bstree
	def initialize(value)
		@root = Node.new(value)
		@inorderlist = []
		puts @root.value
	end

	def addnode(value, root = nil)
		if root == nil
			root = @root
		end

		if root.value >= value
			if root.left != nil
				addnode(value, root.left)
			else
				puts "Adding node to the left"
				root.left = Node.new(value)
			end
		elsif root.value < value
			if root.right != nil
				addnode(value, root.right)
			else
				puts "Adding node to the right"
				root.right = Node.new(value)
			end
		end

	end

	def inorder(root = nil)
		if root == nil
			root = @root
			puts @inorderlist
		end
		
		if root.left != nil
			inorder(root.left)
		else
			@inorderlist.push(root.value)
		end
		@inorderlist.push(root.value)
		if root.right != nil
			inorder(root.right)
		else
			@inorderlist.push(root.value)
		end
	end

end

tree = Bstree.new(2)
tree.addnode(3)
tree.addnode(1)
tree.inorder()
