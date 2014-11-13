#!/usr/bin/python

def generate_matrix_co_ords(index, w, h):
  return index // w, index % w

def generate_neighbors(x, y, w, h, array, threshold):
  result = list()
  for ii in [-1, 1, 0]:
    for jj in [-1, 1, 0]:
      if ii == 0 and jj == 0:
        pass
      elif x + ii >= 0 and x + ii < h and y + jj >= 0 and y + jj < w:
        print x + ii, y + jj
        print '*-*-*-*-*-*-*-*-*-*-*-'
        result.append(array[x * w + y] - array[w * (x + ii) + y + jj])
  if max(result) > threshold:
    return max(result)
  return False

def array_detection(w, h):
  array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
  print generate_neighbors(0, 0, w, h, array, threshold)
array_detection(4, 3)
