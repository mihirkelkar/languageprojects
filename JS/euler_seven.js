/*
10001st prime number
*/
var counter = 0;
var num_count = 2
while(true){
  for(var n = 2; n <= Math.round(Math.sqrt(num_count)); n++){
    if(num_count % n == 0){
      break;
    }
  }
  if(n > Math.round(Math.sqrt(num_count))){
    var prime_number = num_count
    counter += 1
    if(counter == 10001){
      debug(prime_number);
      break;
    }
  }
  num_count++;
}
