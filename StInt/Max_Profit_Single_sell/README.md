The problem here is that you are given stock prices for the N days. You are allowed to buy and sell stock only once. The challange here is to maximize profit. Now in this case, the problem essentially boils down to finding the numbers which has the maximum difference between them. 

The algorithm is as follows:
maintain a maximum_difference. 
maintain a minimum_element found so far. 

Iterate through the array. 
If the difference between the current element and the minimum_element_ever_found is greater than 
max_differnce, then go ahead a nd update max_differnece. 
If current element is less than the min element ever, then go ahead and update the min element
ever. 

maintain an index for the max_difference element too. 
