In this puzzle, given an array A, we need to create an array B such that B[i] is the product of all elements in array A except for the element at index i in A. Also, you cannot use the division operator. 

My approach: 
  Traverse the A array once. 
  All the while filling array B[i] with product until A[i - 1]

 Once that is complete. LEts do a reverse pass over A and B. 
  Now, multilpy B[i] with the element its missed from the right
