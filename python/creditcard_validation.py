#!/usr/bin/python
#Test case is account number 79927398713
#Credit card validation algorithm availbale on Wikipedia

def luhns(card_number):
	card_number_ints = [int(x) for  x in card_number]
	even_places = card_number_ints[-1::-2]
	#print even_places[::-1]
	odd_places = card_number_ints[-2::-2]
	#print odd_places[::-1]
	double_evens = [x * 2 for x in even_places]
	#print double_evens[::-1]
	for i in range(len(double_evens)):
		if double_evens[i] > 9:
	#		print "Entered if"
			#print [int(x) for x in list(str(double_evens[i]))]
			double_evens[i] = sum([int(x) for x in list(str(double_evens[i]))])
	#print double_evens[::-1]
	final = (sum(odd_places + double_evens) * 9) % 10
	return final
def main():
	card_number = raw_input("Enter Account Number")
	if int(card_number[-1]) == luhns(card_number[:-1]):
		print "Valid card by mod10 algorithm"
	else:
		print "Nopenopenopenopenopenopenope"	 

if __name__ == "__main__":
	main()
