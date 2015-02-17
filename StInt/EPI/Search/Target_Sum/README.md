Given an integer X and an unsorted array of integers, describe an algorithm to determine whether two of the numbers add up to x. (You cannot use hashtables in this case)

The way I would do this is sort the given array, I would start from the left of the array and from the right of the array. If th current sum is less than the target, I move the left pointer towards the right. If the current sum is greater than x. I move the right pointer towards the left. 


