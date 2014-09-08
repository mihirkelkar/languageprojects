import sys
fp = open(sys.argv[1], 'r').readlines()
array = []
for ii in fp:
  array.append([int(elem) for elem in ii.strip().split(" ")])
array =  array[::-1]
for ii in range(len(array) - 1):
  for jj in range(len(array[ii]) - 1):
    array[ii + 1][jj] += max(array[ii][jj], array[ii][jj + 1])
print array[-1][-1]
