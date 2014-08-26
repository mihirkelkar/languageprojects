function Node(value){
	this.value = value;
	this.left = null;
	this.right = null;

	this.printInfo = function(){
		debug("The value is " + this.value);
	}
}

function Tree(value){
	var max_result = 0;
	this.root = new Node(value);
	var sum = 0;
	this.calc_max_sum = function(node){
		if(node.left != null){
			sum += node.value;
			this.calc_max_sum(node.left);
		}
		else{
			if(sum >= max_result){
				max_result = sum;
			}
		}
		if(node.right != null){
			sum += node.value;
			this.calc_max_sum(node.right);
		}
		else{
			if(sum >= max_result){
				max_result = sum;
			}
		}
	}
}


tree = new Tree(75);
tree.root.left = new Node(7);
tree.root.right = new Node(4);
tree.root.left.left = new Node(2);
tree.root.left.right = new Node(4);
tree.root.right.left  = new Node(6);
tree.root.left.left.left = new Node(8);
tree.root.left.left.right = new Node(5);
tree.root.right.left.left = new Node(5);
tree.root.right.left.right = new Node(9);
tree.root.right.right.left = new Node(9);
tree.root.right.right.right = new Node(3);
//tree.calc_max_sum(tree.root);

