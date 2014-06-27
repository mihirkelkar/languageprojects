package main 

import "fmt"
//Just checking out basic functionalities with GO.
func main() {
	var myString string
	myString = "Dude"
	myString = myString + "\tAwesome"
	fmt.Println(myString) 
	
	var icelandic string = "Þessi lína er á íslensku."
	fmt.Println(icelandic)
 	fmt.Println(string(myString[1]))
	var integer int
	fmt.Println(integer)
	integer += 1
	fmt.Println(integer)
	integer++
	fmt.Println(integer)
	integer--
	fmt.Println(integer)
}