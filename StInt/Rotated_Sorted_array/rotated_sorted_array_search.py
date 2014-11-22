def rotated_sorted_array_search(array, number):
  high = len(array) - 1
  low = 0
  while low <= high:
    middle = (low + high) / 2
    if number == array[middle]:
      print "Number found"
      return middle
    #Case you have reached a case of the exact point where one list point ends and then rotates. 
    elif array[middle] >= array[middle - 1] and array[middle] > array[middle + 1]:
      #Now decide which direction to go to
      if number > array[middle]:
        print "Number not found"
        print middle 
      elif number < array[middle] and number >= array[0]:
        high = middle - 1
      elif number < array[middle] and number <= array[high]:
        low = middle + 1
    elif array[middle] <= array[middle + 1]:
      if number > array[middle] and number <= array[high]:
        low = middle + 1
      elif number > array[middle] and number > array[high]:
        high = middle - 1
      elif number < array[middle] and number >= array[low]:
        high = middle - 1
      elif number < array[middle] and number < array[low]:
        low = middle + 1

rotated_sorted_array_search([6, 7, 8, 9, 1, 2, 3, 4, 5], 10)


        
