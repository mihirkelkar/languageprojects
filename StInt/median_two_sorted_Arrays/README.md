Median of a sorted array is usually the number which separates the lower half of the array from the higher half of the array. 

We can find the median of two sorted arrays in approximately O(n) time by cpmaring th medians of the two arrays separately. 

So, the idea is to move ahead with the following things : 

Calculate the median of the ar1 and ar2 , call them m1 and m2 respectively. 

Now , go ahead and compare m1 and m2. 
if m1 == m2. return m1

if m1 > m2:
  then the median lies somewhere between ar1[0..n/2]
  and ar2[n/2 .. n - 1]

elif m2 > m1:
  then the median lies somewhere between ar1[n / 2 .. n - 1] to ar2[0 .. n /2]


Keep doing this until the size of both subarrays becomes 2. 
Then the median can be calclated as follows:
  median = max(ar1[0], ar1[1]) + max(ar1[0] + ar1[1]) / 2


