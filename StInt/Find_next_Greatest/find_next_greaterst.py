def find_next_greatest(array, low, high, k):
  while low <= high:
    mid = (low + high) / 2
    if array[mid] > k:
      high = mid - 1
    elif array[mid] < k:
      low = mid + 1
    elif array[mid] == k:
        temp = find_next_greatest(array, mid + 1, high, k)
        if temp == -1:
          return mid + 1
        else:
          return temp + 1
