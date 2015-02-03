Search a sorted array of unknown length. 
Let A be a sorted array whose length is not known in advance. Accessing A[i] for i beyond the end of the array throws an exception. Design an algorithm such that it searches for a key k in Array A and return the index if the element exists or returns -1 if it does not. 


Potential solutions : 
1) Linear search with a time complexity of O(n). 

2) Normal Binary search will not work since the length of the array is unknown.  

3) One sided binary search where we both guess the length of the array and the element key we are looking for . 

  We start from 0 and go ahead by 2's exponenets. Each time we check if the element at that index is actually greater than the element we are looking for or we reach an exception. 
If the element is greater than the one we are looking for we binary search between that exponenet and the last two's exponent for our integer. 

