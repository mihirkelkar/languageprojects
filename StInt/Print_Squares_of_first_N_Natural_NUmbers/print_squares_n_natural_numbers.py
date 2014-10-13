#!/usr/bin/python

def printSquares(number):
  squares = 0
  prev_number = 0
  for ii in range(1, number + 1):
    new_square = squares + prev_number + prev_number + 1
    squares = new_square
    prev_number = ii
    print new_square

def main():
  printSquares(5)

if __name__ == "__main__":
  main()
