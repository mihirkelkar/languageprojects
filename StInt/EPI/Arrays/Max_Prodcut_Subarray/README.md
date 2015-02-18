Given an integer array with negative numbers and zero find the subarray with maximum product. i.e find contiguous array elements that produce maximum product. 


Solution. 

Find out where 0 is in the array. Then split the arrays into sub arrays accordingly and calculate the result for both the arrays. 

So basically iterate till you hit a zero. Lets say you hit a zero at index i
then calculate the product from start_index to i - 1 and store it. 

Next time calculate the product from start_index to i - 1. Keep track from number of negatives you encounter. If you have an odd number of negatives. Keep track of the index of the first and last negative numbers as well. 
  Use the same splitting technique that we used with the zero. To get the max prouct. 
