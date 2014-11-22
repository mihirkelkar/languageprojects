Next Greater Element
=======================
Given an array, print the next greater element for every element. The next greater element for an element x is the first greater element on the right side of x in an array. Elements for twhich no greater element exist, consider next greaterlement as -1. 

Example: 
a) For any array, rightmost element always has the next greater element as -1
b) For an array which is sorted in descending order, all elements have greater element as - 1
c) For an input array [4, 5, 2, 25], the next greater for each element are as
follows.

Element	NGE
4   --> 5
5   --> 25
2   --> 25
25  --> -1

d) For the input array [13, 7, 66, 12] the next greater element for each element are as follows:

There is a linear time soultion available to the problem. 
Start traversing the array in the reverse order, keep a track of the max_element found till a point while iterating. 

Now, that you reach a certain point, check if the number is greater than the number you are iterating on. If it , assign NGE and move on. 
If not, upadte value of max_so_far and move on. Assign it the prev_value for a NGE.  
