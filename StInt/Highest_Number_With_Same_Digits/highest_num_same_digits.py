#!/usr/bin/python

"""
The idea to calculate the highest number  with the same digit is as follow: 
Its a O(n) solution with n being the number of digits with the number. 
Now start from the right most digit in the number. Start moving till you 
find a number which is actually less than its right digit. Les call this digit x
Stop there. Now, find a digit which is the first digit greater that digit x. 
Lets call this digit y. Lets put digit y to the left of digit x. Sort everything to the right of digit y. You're done
"""

def next_highest_with_same_digit(number):
  num_rev = map(int, list(number))[::-1]
  for ii in range(len(num_rev) - 1):
    if num_rev[ii]  > num_rev[ii + 1]:
      break
  #Now lets find the number to the right of the number we found that is just greater than digit x
  #TODO 

next_highest_with_same_digit('123456784987654321')
  
