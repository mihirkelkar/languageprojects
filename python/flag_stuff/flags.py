#!/usr/bin/python

def calc_flags(number_of_colors):
	if number_of_colors == 0 or number_of_colors == 1:
		return 0
	else:
		n = number_of_colors
		temp = 2 * n * (n - 1) * (n - 1)
		temp += (n) * (n -1) * (n - 2)
		temp += (n) * (n - 1) * (n - 2) * (n - 2)
		temp += (n) * (n - 1) * (n - 2) * (n - 2)
		#print temp
		return temp	
def main():
	t = int(raw_input())
	while t != 0:
		print calc_flags(int(raw_input()))
		t -= 1
main()		
