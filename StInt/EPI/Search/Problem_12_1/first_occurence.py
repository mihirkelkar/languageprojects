def return_first_occurence(array, key):
  left = 0
  right = len(array) -1 
  while(left <= right):
    middle = (left + right) / 2
    if array[middle] < key:
      left = middle + 1
    elif array[middle] > key:
      right = middle - 1
    elif array[middle] == key:
      while(array[middle - 1] == array[middle]):
        middle = middle - 1
      return middle
  return -1


def main():
  #test case for the first ocurence. 
  array = [14, -10, -10, 2, 108, 108, 243, 285, 285, 285, 401]
  print return_first_occurence(array, -10)

if __name__ == "__main__":
  main()

