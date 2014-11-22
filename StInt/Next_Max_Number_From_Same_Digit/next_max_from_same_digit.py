#!/usr/bin/python

def next_max_from_same_digits(number):
  for ii in range(len(number) - 1, 1, -1):
    if number[ii] > number[ii - 1]:
      break
    else:
      pass
  if ii != 1:
    number_part_one = number[:ii] + number[]
