#!/usr/bin/python
import random

def random_number_generator(a, b):
  if a == b:
    return a
  else:
    number = 2
    count = 1
    while number <= b - a + 1:
      number *= 2
      count += 1
    while True:
      string = ''
      for ii in range(0, count):
        string += str(random.randint(0, 1))
      if int(string, 2) in range(0, b - a + 1):
        return int(string, 2) + a

def main():
  print random_number_generator(2, 10)

if __name__ == "__main__":
  main()
