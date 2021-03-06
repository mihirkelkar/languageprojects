#!/usr/bin/python
"""
Question : You have an array of 0's and 1's. Determine a window [L,R], such that if you flip the bits in that window, you will have maximum number of 1's in your array, and then output this number of 1's. 

For eg: 
Input array: 1 0 0 1 0 0 1 

Output: 6 

Explanation: 
If you choose a window [1,5], your array becomes, 
1 1 1 0 1 1 1 
which gives the total number of 1's now 6. So, your program should output the number 6, i.e. the maximum number of 1's after choosing a window.
"""

"""
Approach : O(n) Solution. What we can do is maintain a variable called as sum
Find the leftmost zero and start moving ahead. set left_index to the index of the 1 if number == 0 -> sum += 1
if number == 1 , sum -= 1.. Now, if sum hits zero. Then find the next 0 and start again resetting the left_index there. Also keep a count of the max_zeros_seen_so_far
""" 
#This is however exactly equal to the maximum contiguous subsequence problem

def count_max_bits(sequence):
  sequence = map(int, list(sequence))
  #find the leftmost 0
  left_index = sequence.index(0)
  start_index = left_index
  max_number_ever = 0
  sum = 0
  for ii in range(left_index, len(sequence)):
    if ii == 0:
      sum += 1
    elif ii == 1:
      sum -= 1
    if max_number_ever < sum:
      max_number_ever = sum
    if sum <= 0:
      sum = 0
      start_index = left_index
  return max_number_ever
