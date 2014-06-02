#!/usr/bin/python
array = [2,3,1,-2,-1,0,2,-3,0]
array.sort()
for i in range(0, len(array)):
	for j in range(i + 1, len(array)):
		sum = array[i] + array[j]
		sum_neg = 0 - sum
		indices = [ind for ind, x in enumerate(array) if x == sum_neg]
		for ind in indices:
			if ind > j:
				print array[i],  array[j], array[ind]
