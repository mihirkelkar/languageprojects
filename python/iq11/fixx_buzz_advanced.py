#!/usr/bin/python

def advanced_fizz_buzz(a,b):
	fizz = [i for i in range(int(a), int(b) + 1) if i % 3 == 0]
	buzz = [i for i in range(int(a), int(b) + 1) if i % 5 == 0]
	fizzbuzz = list(set(fizz) & set(buzz))
	fizz_new = list(set(fizz) - set(buzz))
	buzz_new = list(set(buzz) - set(fizz))
 	return len(fizz_new), len(buzz_new), len(fizzbuzz)


def main():
	print advanced_fizz_buzz(10000, 213246)

if __name__ == "__main__":
	main()	    