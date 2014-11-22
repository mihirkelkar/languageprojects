#!/usr/bin/python
import heapq

def minimum_finder(matrix, k):
  res = list()
  for index, ii in enumerate(matrix):
    for index2, jj in enumerate(ii):
      res.append((jj, index, index2))
  print res
  print "- - - - - - - - "
  heapq.heapify(res)
  while k > 0:
    temp = heapq.heappop(res)
    print temp
    print matrix[0]
    if temp[2] < len(matrix[0]) - 1:
      res[0] = matrix[temp[1]][temp[2] + 1]
      heapq.heapify(res)
      k -= 1
  return temp[0]
    


def main():
  matrix = [
	   [1, 2, 3],
	   [4, 5, 6],
	   [7, 8, 9] 	
           ]
  print minimum_finder(matrix, 3)

if __name__ == "__main__":
  main()
