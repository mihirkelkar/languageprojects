//Just trying to say whether javascript can be used as a 
//general purpose programming language
function Node(value){
	this.value = value;
	this.next = null;
};

function SinglyLinkedList(){
	this.contruct = function(value){
		this.head = new Node(value);
		this.tail = this.head;
	};

	this.addnode = function(value){
		this.tail.next = new Node(value);
		this.tail = this.tail.next;
	};

	this.print = function(){
		this.cur = this.head;
		while(this.cur != null){
			print(this.cur.value);
			this.cur = this.cur.next;
		};
	}; 

	this.deletealt = function(){
		this.cur = this.head;
		while(this.cur.next != null){
			this.cur.next = this.cur.next.next;
			print(this.cur.value);
			this.cur = this.cur.next;
		}
	} 
};

var newObject = new SinglyLinkedList();
newObject.contruct(1);
newObject.addnode(2);
newObject.addnode(3);
newObject.addnode(4);
newObject.addnode(5);
newObject.deletealt();