def same_index_element(array):
  left = 0
  right = len(array) - 1
  while left < right:
    middle = (left + right) / 2
    if array[middle] > middle:
      right = middle - 1
    elif array[middle] < middle:
      left = middle + 1
    elif array[middle] == middle:
      return middle
  return -1

def main():
  array = [-2, 0, 2, 3, 6, 7, 9]
  print same_index_element(array)

if __name__ == "__main__":
  main()    
