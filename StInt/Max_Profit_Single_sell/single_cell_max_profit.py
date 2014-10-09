#!/usr/bin/python

def find_max_single_profit(arr):
  max_difference = 0
  min_element = arr[0]
  max_element = arr[0]
  buying_price = None
  for ii in range(1, len(arr)):
    if arr[ii] - min_element > max_difference:
      max_difference = arr[ii] - min_element
      max_element = arr[ii]
      buying_price = min_element
    if arr[ii] < min_element:
        min_element = arr[ii]
  return max_difference, buying_price, max_element
def main():
  array = [70, 76, 73, 72, 75]
  max_diff, min_el, max_el = find_max_single_profit(array)
  print "The max profit generated is %s" %max_diff
  print "The buying price would be %s" %min_el
  print "The selling price should be %s" %max_el

if __name__ == "__main__":
  main()
