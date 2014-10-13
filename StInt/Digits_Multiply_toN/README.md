Given a number 'n', find the smallest number p such that if we multiply all the digits of p, we can get n. The result p should have minimum two digits. 

Example I/P : n = 36
O / P : 49.

Example n = 100
O / P : 455.

Approach: 

For any numnber n if the number is less than 9 , then just go ahead and add ten to the number. 

Now, for the numbers greater than 10, go ahead and break the number into its factors between 2 and 9 preferentially begin from 9 and move to 2. 

If thats not possible. print not possible. 

Now reverse the array and boom. You have your number. 


