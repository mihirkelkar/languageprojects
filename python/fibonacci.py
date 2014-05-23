#!/usr/bin/python
def fibo(number):
	if number == 0 or number == 1:
		return number
	else:
		stuff = fibo(number - 1) + fibo(number - 2)
		return stuff
		
def main():
	number = input("please enter the number till which you want the fibonacci calculated")
	print fibo(number)

if __name__ == "__main__":
	main()
