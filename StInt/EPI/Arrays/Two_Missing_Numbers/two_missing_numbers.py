#We can take the O(n) approach and list the numbers in a hash map. 

"""
However, lets try and make a better technique. We calculate the sum of the n - 2 numbers and the sum of all numbers from 1 to n is n*(n+1) / 2. The sum of all numbers squared from 1 to n is n*(n+1)*(2n+1) / 6. 
Subtract the actual sum from the n(n+1) / 2 and the actual sum of squares from 
n(n+1)(2n+1)/6. You will now have a + b and a^2 + b^2. That can be used to find 2ab. and thus a and b. 
"""
import math

def find_missing_numbers(array):
  sum_of_array = (len(array) + 2)*(len(array) + 3) / 2
  sum_of_array_square = (len(array) + 2) * (len(array) + 3) * (2 *(len(array)+2) + 1) / 6 
  actual_sum = sum(array)
  actual_square_sum = 0
  for ii in array:
    actual_square_sum += ii ** 2
  xplusy = sum_of_array - actual_sum
  xsquareysquare = sum_of_array_square - actual_square_sum
  twoxy = xplusy ** 2 - xsquareysquare
  xminusy = math.sqrt(xsquareysquare - twoxy)
  x = (xplusy + xminusy) / 2
  y = (xplusy - xminusy) / 2
  print x
  print y

def main():
  find_missing_numbers([1, 2, 3, 4, 5, 7, 8])

main()
