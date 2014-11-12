#!/usr/bin/python

"""
Using a divide and conquer technique. 
"""
def find_min_max(array):
  high = len(array)
  low = 0
  mid = (low + high) / 2
  if len(array) <= 2:
    return (min(array), max(array))
  else:
    left = find_min_max(array[low:mid])
    right = find_min_max(array[mid:high])
    return (min(min(left), min(right)), max(max(left), max(right)))

def main():
  print find_min_max([4, 1, 0, 5, 7, 3])

if __name__ == "__main__":
  main()
