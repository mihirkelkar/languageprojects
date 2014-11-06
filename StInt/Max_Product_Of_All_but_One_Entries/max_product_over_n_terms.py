#!/usr/bin/python

def calculate_leave_one_out(array):
  flag = True
  negative_count = 0
  positive_count = 0
  min_positive = 0
  product = 1
  max_neg = None
  for ii in range(len(array)):
    if array[ii] == 0:
      leave_out = ii
      flag = False
    elif array[ii] < 0:
      negative_count += 1
      if max_neg == None:
        max_neg = ii
      elif array[ii] > array[max_neg]:
        max_neg = ii
    elif array[ii] > 0:
      positive_count += 1
      if array[ii] < array[min_positive]:
        min_positive = ii
  if flag:    
    if negative_count % 2 == 0:
      leave_out = min_positive
    else:
      leave_out = max_neg

  for ii in range(len(array)):
    if ii != leave_out:
      product *= array[ii]
  return product
  
def main():
  print calculate_leave_one_out([1, 2, 3, 4, 5, -1, -2, -3, -4])

if __name__ == "__main__":
  main()
