


def splitstring(s):
	result = [s]
	for i in range(1, len(s)):
		result.extend('%s %s' % (s[:i], x) for x in splitstring(s[i:]))
	return result


choice = raw_input("Enter the string")
result =  splitstring(choice)
for i in result:
	flag =  1
	temp  = [int(x) for x in i.split(" ")]
	#print temp
	for i in range(0, len(temp)):
		if temp[i] < 27:
			temp[i] += 96
			temp[i] = chr(temp[i])
		else:
			flag = 0
			break
	if flag == 1:
		print (" ").join(temp)			
