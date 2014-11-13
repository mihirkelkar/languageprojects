def construct_triangle(array):
  if len(array) == 1:
    return
  else:
    temp = [array[ii] + array[ii + 1] for ii in range(0, len(array) - 1)]
    construct_triangle(temp)
    print temp

construct_triangle([4, 7, 3, 6, 7])

