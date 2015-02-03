def occurence_greater_than(array, key):
  left = 0
  right = len(array) - 1
  while(left <= right):
    middle = (left + right)/ 2
    if array[middle] < key:
      left = middle + 1
    elif array[middle] > key:
      right = middle - 1
    elif array[middle] == key:
      while(True): 
        if middle == len(array) - 1 or array[middle] == array[-1]:
          return -1
        else:
          if array[middle + 1] == array[middle]:
            middle += 1
          else:
            return middle + 1

def main():
  array = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
  print occurence_greater_than(array, -14)
    

if __name__ == "__main__":
  main()
