Given an integer array , move all the zeroes to the right side of the array with as little swaps as possible. 

The idea is to maintain two different poitners. One is called the left pointer and the other is called the right pointer. 

If the left pointer has a zero and the right pointer has a non zero, then we exchange and move the right pointer slightly to the left hand side. 

We continue this until both pointers dont cross or equal each other. 
