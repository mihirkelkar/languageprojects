Given a sorted array and a number k, find the next number greater in the arary than the number just provided.

1) Approach : Do a binary search to find the number. 
  2) Do a binary search on the right subarray to find the last occurence of that number. 
  --> Add 1 to it and return unless its the last element or its -1. 

Return -1 if the number is not found. 

//SUM BUGS HERE

 
