package main 

import "fmt"

type Node struct{
	value int
	next *Node
}

func main(){
	node_one := Node{1, nil}
	fmt.Println(node_one.value)
}