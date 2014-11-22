def selection_sort(list):
  for ii in range(0, len(list) - 1):
    min_element_index = list.index(min(list[ii:]))
    list[ii], list[min_element_index] = list[min_element_index], list[ii]
  return list

def main():
  print selection_sort([5, 4, 3, 2, 1])

if __name__ == "__main__":
  main()
