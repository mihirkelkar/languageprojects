#!/usr/bin/python

def median_of_two_sorted_arrays(array_one, array_two):
  print array_one
  print "=============="
  print array_two
  print "=============="
  if len(array_one) != len(array_two):
    return 
  else:
    if len(array_one) == 2:
      median = (max(array_one[0], array_two[0]) + min(array_one[1], array_two[1])) / 2
      print median
    else:
      median_one = (0 + (len(array_one) - 1)) / 2
      median_two = (0 + (len(array_two) - 1)) / 2
      if array_one[median_one] == array_two[median_two]:
        print array_one[median_one]
      elif array_one[median_one] > array_two[median_two]:
        median_of_two_sorted_arrays(array_one[0:median_one + 1], array_two[median_two:])
      elif array_one[median_one] < array_two[median_two]:
        median_of_two_sorted_arrays(array_one[median_one:], array_two[0:median_two + 1])

def main():
  median_of_two_sorted_arrays([1, 12, 15, 26, 38], [2, 13, 17, 30, 45])

if __name__ == "__main__":
  main()  
