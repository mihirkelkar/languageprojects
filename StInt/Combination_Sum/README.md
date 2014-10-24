Given a collection of candidate numbers, and a target. Find all combinations withtin the list that can sum to that number. 

This can have a recursive solution. 

Pick the first index. 

if sum < target_number, then do a binary search for target - sum. If not, then simply pick the next index. and pass it on, add it to sum and pass it on. 

If == target, then go ahead and append it to the solution. 