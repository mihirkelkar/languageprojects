class Node{
	Node prev;
	Node next;
	Node child;
	int value;
	public Node(int data){
		value = data;
	}
	public void addchild(int data){
		child = new Node(data);		
	}
	
}

class Doublelinkedlist{
	Node head;
	Node tail;
	public Doublelinkedlist(){
		head = null;
		tail = null;
	}
	public void addnode(int data, Node cur){
		if(head == null){
			head = new Node(data);
			tail = head;
		}
		else{
			if(cur == tail){
				tail.next = new Node(data);
				tail = tail.next;	
			}
			else{
				cur.next = new Node(data);
			}

		}
	}	

	public void printlist(Node cur){
		while(cur != null){
			System.out.println(cur.value);
			if(cur.child != null){
				System.out.println("+++++");
				printlist(cur.child);
				System.out.println("+++++");
			} 
			cur = cur.next;	
		}
	}

	public void flatten(Node cur){
		while(cur != null){
			if(cur.child != null){
				Node temp = cur.next;
				Node tmpr = cur.child;
				cur.next = tmpr
				while(tmpr.next != null){
					tmpr = tmpr.next;
				}
				tmpr.next = temp;
				cur.child = null;
			}
		cur = cur.next;		
		}
	}

}