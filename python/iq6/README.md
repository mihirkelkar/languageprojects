input [2,3,1,4] 
output [12,8,24,6] 

Multiply all fields except it's own position. 

Restrictions: 
1. no use of division 
2. complexity in O(n)



Solution: 
arr = 2, 3, 1, 4

// maintain two arrays which can be done in O(n)

arr1 = 2,  6,   6,  24 (arrays multiply each number with previous and current)
arr2 = 24, 12, 4, 4    (arrays multiplied from end)

In above two arrays, put 1 in beginning of arr1 and end of arr2:
arr1 = 1, 2,  6,   6,  24, 1
arr2 = 24, 12, 4, 4,   1

Then to find number at index 'i' you would just do:

arr1[i]*arr2[i+1]
