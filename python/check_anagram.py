#!/usr/bin/python

def make_map(string):
	map = {}
	for ii in string:
		try:
			map[ii] += 1
		except:
			map[ii] = 1
	return map
				
def check_anagram(string_one, string_two):
	map_one = make_map(string_one)
	map_two = make_map(string_two)

	if map_one == map_two:
		print "Confirmed anagrams"
	else:
		print "Not anagrams"	

def anagram_check_two(string_one, string_two):
	string_one = string_one.lower()
	string_two = string_two.lower()
	if sorted(string_one) == sorted(string_two):
		print "Confirmed anagrams by second function"
	else:
		print "Not anagrams"	

def main():
	check_anagram('racecar', 'carrac')
	anagram_check_two('racecar', 'carrac')

if __name__ == "__main__":
	main()		