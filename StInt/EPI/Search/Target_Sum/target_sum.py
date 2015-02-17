def target_sum(array, target):
  array = sorted(array)
  left = 0
  right = len(array) - 1
  while left < right:
    if array[left] + array[right] == target:
      print left, right
      break
    elif array[left] + array[right] < target:
      left += 1
    elif array[left] + array[right] > target:
      right -= 1
  

target_sum([1, 2, 3, 4, 5], 8)
