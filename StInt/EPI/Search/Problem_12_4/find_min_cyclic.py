def find_min_cyclic(array):
  left = 0
  right = len(array) - 1
  while left < right:
    middle = (left + right) / 2
    if middle != 0:
      if array[middle] < array[middle + 1] and array[middle - 1] < array[middle]:
        if array[middle] > array[0]:
          left = middle + 1
        elif array[middle] < array[0]:
          right = middle - 1
      elif array[middle] < array[middle + 1] and array[middle] < array[middle - 1]:
        return array[middle]
  return -1


def main():
  array = [378, 478, 550, 631, 103, 203, 220, 234, 279, 368]
  print find_min_cyclic(array)

if __name__ == "__main__":
  main()
