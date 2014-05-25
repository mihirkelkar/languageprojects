def palindrome(string : String) : Unit = {
	if(string.length > 1)
	{
		if(string(0) == string(string.length - 1))
			{
				palindrome(string.substring(1, string.length  - 1))
			}
		else
			{
				println("Not a palindrome")
			}
	}
	else
	{
		println("Palindrome")	
	}


}

println("Please enter your required text")
var string = readLine().toLowerCase.replace(" ", "")
//println(string)
palindrome(string)
