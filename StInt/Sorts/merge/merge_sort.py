def merge_sort(list):
  if len(list) <= 1:
    return list
  middle = (0 + len(list)) / 2
  left_list = merge_sort(list[:middle])
  right_list = merge_sort(list[middle:])
  return merge(left_list, right_list)


def merge(left_list, right_list):
  new_list = list()
  while left_list and right_list:
    if left_list[0] <= right_list[0]
      new_list.append(left_list.pop(0))
    else:
      new_list.append(right_list.pop(0))
  if left_list:
    new_list  += left_list
  elif right_list:
    new_list += right_list
  return new_list    
