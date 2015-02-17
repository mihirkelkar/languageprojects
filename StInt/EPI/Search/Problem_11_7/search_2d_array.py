def search_2d_array(array, key):
  for ii in range(0, len(search_2d_array)):
    if ii[0] < key:
      print "Element has not been found"
      break
    else:
      if ii[-1] >= key:
        if binary_search(ii, key):
          break
          print "found"
      else:
        continue


def binary_search(array, key):
  high = len(array)
  low = 0
  mid = (low + high) / 2
  while low < high:
    if array[mid] == key:
      return True
    else:
      if array[mid] < key:
        low = mid
      elif array[mid] > key:
        high = mid
  return False

