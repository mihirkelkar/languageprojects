#Encryption for letter x : E(x) = (x + n)mod26
#Decryption for letter x : D(x) = (x - n)mod26
#n is the number of shifts possible

text = raw_input("Enter the text").lower()
shift = input("Enter the number of shifts you want")
decrypt_text = ""
for i in text:
	temp = ord(i) + (shift % 26)
	if temp > ord('z'):
		temp = temp % ord('z')
		temp = ord('a') + temp - 1
	print chr(temp)
print decrypt_text
