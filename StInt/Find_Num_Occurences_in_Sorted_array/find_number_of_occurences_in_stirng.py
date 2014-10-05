#The idea here is to use a function that basically does a binary search and looks for the lement. 
#Once my element is found, it does a binary search to the left and to the right and then returns
#how many more instances were found

def find_occurences(array, el, start = 0, end = len(array) - 1):
  if start > end:
    return 0
  mid = (start + end)/ 2
  if el > array[mid]:
    count = find_occurences(array, el, start = mid + 1)
  elif el < array[mid]:
    count = find_occurences(array, el, end = mid - 1)
  elif el == array[mid]:
    count = 1 + find_occurences(array, el, start = mid + 1) + find_occurences(array, el, end = mid - 1)
  return count

  
