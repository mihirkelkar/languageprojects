def check_palindrome(string):
	if len(string) > 1:
		if string[0] == string[-1]:
			check_palindrome(string[1:][:-1])
		else:
			print "Not a palindrome"
	else:
		print "Palindrome"

text = raw_input("Please enter your text string")
check_palindrome(text.lower().replace(" ",""))
