Given a collection for intervals, merge all overlapping intervals. 

For example, 

Given : [1, 3], [2, 6], [8, 10], [15, 18]
Return : [1, 6], [8, 10], [15, 18]. 

The solution is to sort the arrays by their point of start and then look for possible cases where the following element starts before the preceding element ends. 
