Given a sorted array of unkown length and a number to serach for, return the index of the number in the array. Accessing an element out of bounds throws exception. 

Stragitht forward solution : Keep scanning the array until of couse you either 
run into the element itself or you come accross an exception. 

However, we can also make use of a modified binary search feature in this case. Lets say we're searching for the value k. We check array indexes 0, 1, 2, 4, 8, 16, 2 ** N in a loop until either we get an exception or we see an element larger than k. 

Then we do a binary search from 2 ^ (k - 1) till 2^k - 1. 
