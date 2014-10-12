#!/usr/bin/python

def reverse_digits(number):
  reverse = 0
  neg = 0
  if number < 0:
    neg = 1
    number = number * -1
  while(number):
    result = result * 10 + number % 10
    number = number / 10
  if neg == 1:
    return result * -1
  return result
