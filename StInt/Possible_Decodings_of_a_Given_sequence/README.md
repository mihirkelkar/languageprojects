Let 1 represent ‘A’, 2 represents ‘B’, etc. Given a digit sequence, count the number of possible decodings of the given digit sequence.

Examples:

Input:  digits[] = "121"
Output: 3
// The possible decodings are "ABA", "AU", "LA"

Input: digits[] = "1234"
Output: 3
// The possible decodings are "ABCD", "LCD", "AWD"
An empty digit sequence is considered to have one decoding. It may be assumed that the input contains valid digits from 0 to 9 and there are no leading 0′s, no extra trailing 0′s and no two or more consecutive 0′s.

My approach: generating all differnet combinations of  the numbers actually depends on how we mainpulate space within the number string. 

Lets write a recursive function to do that. 

Retrieve the entire list, run through it to see if the any of the numbers generated are not greater than 26. If that is the case, disregard that entry and move on. 
