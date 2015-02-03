def unknown_length_binary_search(array):
  counter = 0
  prev_index = 0
  flag = True
  while True:
    try:
      if array[2**counter] < key:
        prev_index = 2**counter
        counter += 1
      elif array[2**counter] == key:
        return 2**counter
      else:
        break
    except IndexError:
      break
  
  #however, we need a try except case even within the binar search for the eventuality
  #that we have broken out of the above step with an exception. 
  
  left = prev_index
  right = (2**current) - 1
  while left < right:
    try:
      mid = (left + right) / 2
      if array[mid] == key:
        return mid
      elif array[mid] > key:
        right = mid - 1
      elif array[mid] < key:
        left = mid + 1
    except:
      right = right - 1  
  return -1     
        
 
