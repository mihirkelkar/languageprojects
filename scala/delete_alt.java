class Node{
	int data;
	Node next;

	public Node(int data){
		data = data;
		next = null;
	}
}

class SinglyLinkedList{
	Node head;
	Node tail;

	public SinglyLinkedList(){
		head = null;
		tail = null;
	}

	public void addNode(int data){
		if(head == null){
			head = new Node(data);
			tail = head;
		}
		else
		{
			tail.next = new Node(data);
		}
	}

	public void printList(){
		Node cur = head;
		while(cur != null){
			System.out.println(cur.data);
			cur = cur.next;
		}
	}


	public static void main(String[] args){
		SinglyLinkedList single = new SinglyLinkedList();
		single.addNode(1);
		single.addNode(2);
		single.addNode(3);
		single.addNode(4);
		single.addNode(5);
		single.printList();
	}
}