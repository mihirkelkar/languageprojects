Fizz Buzz is a simple game used to teach kids about divisibility. The goal of the game is to say positive integers in increasing order, with a twist: You don't say the numbers divisible by 3 and 5. Instead, whenever a number was divisible by 3 you say "fizz" and for a number divisible by 5 you say "buzz". (Thus, if a number was divisible by 15, you say "fizzbuzz".)

Here is how the game starts: 1, 2, fizz, 4, buzz, fizz, 7, 8, fizz, buzz, 11, fizz, 13, 14, fizzbuzz, 16, 17, fizz, 19, buzz, fizz, 22, 23, fizz, buzz, 26, fizz, 28, 29, fizzbuzz, 31, 32, fizz, 34, buzz, fizz, ...

Fizz Buzz has also become a traditional programming interview question. However, in this problem we have a more tricky assignment for you.

You are given longs A and B. Consider the part of the game that corresponds to integers from A to B, inclusive. During this part of the game, you will say "fizz" X times, "buzz" Y times, and "fizzbuzz" Z times. Return a long[] with three elements: {X,Y,Z}.

Inputs: 
1
4
Output: {1, 0, 0}

2
6
Output: {2, 1, 0}