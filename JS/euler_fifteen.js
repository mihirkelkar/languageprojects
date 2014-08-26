/*
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?

*/


//Most elegant solution to the up and righ tmoves in the lattice problem ever
//No dynamic programming needed

//If you select the number of right turns from a possible total turns, 
//The number of down turns will arrange themselves. So do a gridsize C (gs / 2)

function transit(gridsize){
  var total_product = 1;
  var one_way_factorial = 1;
  for(i = 1; i <= gridsize * 2; i++){
    total_product *= i;
  }
  for(i = 1; i <= gridsize; i++){
    one_way_factorial *= i; 
  }

  //sqaured coz. NcR is n!/r!(n - r)!
  var total_paths = total_product /(one_way_factorial * one_way_factorial);
  return total_paths;
}

debug(transit(20));
