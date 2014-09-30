#!/usr/bin/python
"""
Given two positive integers, compute their quotient, using only the addition, subtraction, and shifting operators. 
"""

def division(dividend, divisor):
  quotient = 1
  #Check if they are the same number. 
  if dividend == divisor:
    remainder = 0
    return quotient, remaninder
  #Check if the dividend is actually less than the divisor
  elif dividend < divisor:
    return 0, dividend
  #Other normal case when the dividend is actually greater than divisor
  else:
    quotient = 0
    increments = divisor
    while(dividend >= divisor):
      quotient += 1
      temp_divisor = divisor
      print "temp_divisor : %s" %temp_divisor
      divisor += increments
      print "divisor : %s" %divisor
    remainder = dividend - temp_divisor
    print "remainder : %s" %remainder
    return quotient, remainder

def main():
  print division(100, 8)

if __name__ == "__main__":
  main()
