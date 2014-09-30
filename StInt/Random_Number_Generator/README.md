Construct a Random Number generator whcih produces random numbers between a and b inclusive. The function uses an uqually likely distributed random number generator whic wither returns a zero or a one. Make the newer random number generator such that all returned numbers are equally likely. 


Approach: Generating random numbers between a to b is technically equal to generating random numbers between 0 and b - a and then just adding a to them. 
I can produce such a number directly by concatanating values by the internal random number generator. The trick however is to generate the exact length of this sequence. 
So find the integer i such that 2^i == b - a or really just higher. 
Now if 2^i is exactly equal to b - a then great. Return any number you find. 
else check whether the number you generated is within your stipulated range of numbers

