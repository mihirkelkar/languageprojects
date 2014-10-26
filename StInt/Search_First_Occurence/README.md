Write a method that takes a sorted array A and a key k and returns the index of the first occurence of k in A. Return -1 if k does not appear. 

Idea : 
 1) Use binary search to find the element. 
2) Once you have found the element, then still do a binary search on the left sub array to make sure that this is the first occurence. 

