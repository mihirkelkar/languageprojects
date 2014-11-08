In a grid farm, every cell is either 'Y' or 'N'. 'Y' means the cell has grass in it, and 'N' means the cell is empty.  


If two adjacent cells have grass, they will belong to a common field. The same applies if there are more than 2 adjacent cells with grass. That is, if cell X is adjacent to cell Y and cell Y is adjacent to cell Z, then cell X will be considered adjacent to cell Z and they will lie in the same field. If a cell doesn't have any adjacent cell with grass, then it will also be a field.

 

Every field must feed one sheep or one cow. Each field of grass cannot be shared between cows and sheep. If each field can have one sheep or one cow and never both, how many possible unique arrangements can you make such that, there are even number of sheeps in the grid farm?

 

Input:
The first line contains R (number of rows) and C (number of columns)
Each of the next R lines contains a string with length equal to C, and the string is composed of 'Y' and/or 'N'.


Output:
S % 1000000007, S is an integer

Constraint:
1 <= R, C <= 5000

Sample Input:

3 4
YNNY
NYNY
NYNN
 



Sample Output:

4
Explanation:

First Solution
Cow
Cow
Cow
Second Solution
Sheep
Cow
Sheep
Third Solution
Sheep
Sheep
Cow
Fourth Solution
Cow
Sheep
Sheep

