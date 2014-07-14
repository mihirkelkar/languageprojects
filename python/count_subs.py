#!/usr/bin/python
"""
Each string consists of only 0s and 1s. Find all substrings which begin with a 1 and end in a 1. The first line of the input contains the total number of test cases, the second line of input is the max length of the substring.
"""
tt = input()
while(tt > 0):
  n = input()
  string = raw_input().strip()
  counter = 0
  for ii in range(0, len(string)):
    if string[ii] == '1':
      for jj in range(ii, len(string)):
        if string[jj] == '1':
          if jj - ii <= n:
            counter += 1
  print counter
  tt -= 1
        
