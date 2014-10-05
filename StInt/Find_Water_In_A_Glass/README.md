
u can put water to only top glass. If you put more than 1 litre water to 1st glass, water overflows and fills equally in both 2nd and 3rd glasses. Glass 5 will get water from both 2nd glass and 3rd glass and so on.
If you have X litre of water and you put that water in top glass, how much water will be contained by jth glass in ith row?

Example. If you will put 2 litre on top.
1st – 1 litre
2nd – 1/2 litre
3rd – 1/2 litre

Caclualte to tal number of glasses in the set. 
Initialize and empty array with zeroes of the length of the total number of glasses. 

Basically iterate through each row 
  iterate through each column 
    --> Fill it either to capacity, or to whatever is possible. 
    --> Calculate overflow. 
    --> Fill up its children in the array. 
