/*
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
*/

var sum_of_squares = 0;
var square_of_sums = 0;
for(var ii = 0; ii < 101; ii ++){
  sum_of_squares += ii * ii;
  square_of_sums += ii; 
}
debug("The difference between the sums of squares and square of sum is ")
debug(sum_of_squares - (square_of_sums * square_of_sums));
