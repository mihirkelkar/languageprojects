def longest_subarray(array):
  start_index = 0
  subarray_length = 0
  longest_subarray = list()
  while start_index != len(array) - 1:
    subarray = list()
    hash = {}
    distinct = True
    for ii in range(start_index, len(array)):
      try:
        temp = hash[array[ii]]
        distinct = False
        break
      except:
        hash[array[ii]] = 1
        subarray.append(array[ii])
    if len(hash.keys()) > subarray_length:
      subarray_length = len(subarray)
      longest_subarray = subarray
    start_index += 1
  return longest_subarray

def main():
  print longest_subarray([5, 5, 26, 3, 1,6, 6, 3])

main()
