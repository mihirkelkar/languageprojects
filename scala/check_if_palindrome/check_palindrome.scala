var ip = readLine("Enter a string to check if its a palindrome\n").toLowerCase()
var ip_new = ip.replace(" ","")
if(ip_new == ip.reverse){
	println("Is a palindrome")
}
else{
	println("Not a palindrome")
}
