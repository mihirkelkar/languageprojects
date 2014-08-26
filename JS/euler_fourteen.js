//Writing code for the collatz conjecture in JAvaScript. This is Project Euler Problem no 14

//n -> n / 2
//n -> 3n + 1

var i = 0;
var max_count = 0;
var max_count_holder = 1;
for(i = 1; i < 1000000; i++){
  var number = i;
  var counter = 0;
  while(number != 1){
    counter++;
    if(number % 2 == 0){
      number = number / 2;
    }
    else{
      number = 3 * number + 1;
    }
  }
  if(counter > max_count){
    max_count = counter;
    max_count_holder  = i;
  }
}
debug("The longest collatz series until a million is by" + max_count_holder);
