package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main(){
	reader := bufio.NewReader(os.Stdin)
	fmt.Println("Enter word to be converted into pig latin")
	text,error := reader.ReadString('\n')
	text = strings.ToLower(text)
	text = text[:len(text) - 1]
	fmt.Printf("%v\n", error)
        if strings.Contains("aeiou", string(text[0])){
			text = text + "way"
			fmt.Println(text)				
		}else{
		var tmp string = text 
		for i := 0; i < len(text); i++{
			if strings.Contains("aeiou", string(text[i])){
				break
			}else{
				tmp = tmp[1:] + string(text[i])  
			}
		}
		fmt.Println(tmp + "ay")
		
	}
}
