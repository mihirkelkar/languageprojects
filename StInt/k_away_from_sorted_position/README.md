The input consists of a very long sequence of numbers. Each number
is at most k positions away from its correctly sorted position. Design an algorithm that
outputs the numbers in the correct order and uses O(k) storage, independent of the number
of elements processed.

""""""""""""  GOLD STANDARD FOR DATA STRUCTURE USE ? 
Approach: The idea is to maintain a min heap which consists of k + 1 elements. So basically after you have k + 1 elements iterated through. always take the min element out and insert the new one in and heapify
