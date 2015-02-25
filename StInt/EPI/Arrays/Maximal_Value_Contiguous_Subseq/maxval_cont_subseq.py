def maxval_cont_subseq(array):
  max_val_array = list()
  max_val_array.append(array[0])
  for ii in range(1, len(array)):
    max_val_array.append(max(max_val_array[ii - 1] + array[ii], array[ii]))
  return max_val_array[-1]

def main():
  print maxval_cont_subseq([1, -1, 4, 5, -3, 3])


if __name__ == "__main__":
  main()
