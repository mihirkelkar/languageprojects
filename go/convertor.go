package main 

import (
	"fmt"
)

func convert_temp(){
	var ipchoice int
	var temp float32
	fmt.Println("Enter your input unit\n1.Farheniet\n2.Celcius")
	fmt.Scan(&ipchoice)
	fmt.Println("Enter the Temperature value")
	fmt.Scan(&temp)
	if ipchoice == 1{
		var opvalue = ((temp - 32) * 5) / 9
		fmt.Printf("Your value converted to celcius is %.2f\n", opvalue)
	} else {
		var opvalue = (temp * 9 / 5) + 32
		fmt.Printf("Your value converted to Farheniet is %.2f\n", opvalue)
	}
}




func main() {
	fmt.Println("Convertor\n1.Temperature")
	var i int
	fmt.Scan(&i)
	if i == 1{
		convert_temp()	
}