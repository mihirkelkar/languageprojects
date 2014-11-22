Sort all the elements in a given stack using another stack. 

The trick here is to pop the element in the orig stack. Check if the top of S2 is greater than the popped element. If it is then just ush it onto s2, else pop all elements out of s2 which are greater than popped element and push them onto s1. Then push the initially popped element onto s2. 
