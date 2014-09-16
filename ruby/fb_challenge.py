#A possible solution to this uqestion would be to go from 1 to the sqrt of the input number, subtracting squares of values from the actual number. 
#If the resultant number is a perfect square, then we have a macth
import math
import sys

def find_perfect_squares(number):
  count = 0
  print "=========="
  number_sqrt = int(math.sqrt(number)) + 1
  for ii in range(number_sqrt):
    jj = number - ii * ii
    if math.sqrt(jj) == int(math.sqrt(jj)):
      count += 1
      print jj
  return count

fp = open(sys.argv[1], 'r').readlines()
for ii in fp:
  print find_perfect_squares(int(ii.strip()))
