def longest_increasing_subarray(array):
  start = 0
  end = 0
  longest_sub_array = 0
  max_start = 0
  max_end = 0
  for ii in range(1, len(array)):
    if array[ii] > array[ii - 1]:
      end = ii
    else:
      start = ii
      end = ii
    if end - start > longest_sub_array:
      longest_sub_array = end - start
      max_start = start
      max_end = end
  return max_start, max_end

def main():
  print longest_increasing_subarray([2, 11, 3, 5, 13, 7, 19, 17, 23])

if __name__ == "__main__":
  main()
