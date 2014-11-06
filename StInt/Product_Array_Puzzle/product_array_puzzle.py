def product_puzzle(array):
  new_array = [None for ii in range(len(array))]
  temp = 1
  for ii in range(len(array)):
    new_array[ii] = temp
    temp *= array[ii]

  temp = 1
  for ii in range(len(array) - 1, -1, -1):
    new_array[ii] *= temp
    temp *= array[ii]

  return new_array

def main():
  print ' - - - - - - - - - -'
  print product_puzzle([1, 2, 3, 4, 5])
  print ' - - - - - - - - - -'
  
if __name__ == "__main__":
  main()
