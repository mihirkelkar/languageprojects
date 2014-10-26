#!/usr/bin/python

def search_first_occ(array, high, low, k):
  while (low <= high):
    mid = (low + high) / 2
    if array[mid] > k:
      high = mid - 1
    elif array[mid] < k:
      low = mid + 1
    elif array[mid] == k:
      if search_first_occ(array, mid - 1, low, k) == -1:
        return mid
  return -1
