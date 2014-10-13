#!/usr/bin/python

def find_nth_number(n):
  numbers = [3, 4]
  count = 0
  while count < n:
    number = numbers.pop(0)
    count += 1
    for ii in ['3', '4']:
      numbers.append(str(number) + ii)
  print number

def main():
  find_nth_number(3)

if __name__ == "__main__":
  main()
