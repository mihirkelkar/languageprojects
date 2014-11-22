def find_next_highest_number(number):
  number = str(number)
  pivot = None
  for ii in range(len(number) - 1, 0, -1):
    if int(number[ii]) > int(number[ii - 1]):
      pivot = ii - 1
      break
  if pivot is not None:
    number_part_right = sorted(list(number[pivot + 1:]))
    number_part_left = list(number[0:pivot + 1])
    number_part_left[-1], number_part_right[0] = number_part_right[0], number_part_left[-1]
    number_part_right = sorted(number_part_right)
    number = number_part_left + number_part_right
    print number_part_left
    print number_part_right
  return int(''.join(number))

print find_next_highest_number(3452)
