def move_zeroes_to_right(array):
  left_ptr = 0
  right_ptr = len(array) - 1
  while left_ptr <= right_ptr:
    if array[left_ptr] == 0 and array[right_ptr] != 0:
      array[left_ptr], array[right_ptr] = array[right_ptr], array[left_ptr]
      left_ptr += 1
      right_ptr -= 1
    elif array[left_ptr] == 0 and array[right_ptr] == 0:
      right_ptr -= 1
    elif array[left_ptr] != 0:
      left_ptr += 1
  return array

def main():
  print move_zeroes_to_right([1, 0, 0, 9, 2, 0, 4, 9])

if __name__ == '__main__':
  main()
