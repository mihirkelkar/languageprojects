Given an n * n matrix, where every row and column in sorted in non-decreasing order. Find the kth smallest element in a 2d array. 

eg. 
For example, consider the following 2D array.

        10, 20, 30, 40
        15, 25, 35, 45
        24, 29, 37, 48
        32, 33, 39, 50
The 3rd smallest element is 20 and 7th smallest element is 30

The way to to do this is to leverage the min-heap:
  1) Build a min heap of elements in the first row. A heap entry also stores row number and column number. 

  2) Now do the followinf k times. 
    --> Get minimum element from min heap. 
    --> Find row number and column number of the minmum element. 
    --> Replace root with the next element from the same column and min hea        pify the root. 

  3) Return the last extracted root. 
