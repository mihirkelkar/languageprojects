package main 

import "fmt"

type Position struct{
	x int
	y int
}

func main(){
	pos := Position{1,1}
	fmt.Printf("{x : %d, y : %d}\n", pos.x, pos.y)
}