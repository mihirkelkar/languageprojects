import util.control.Breaks._
var counter = 0
var prime = 3
var sum = 2
while(true){
  var prime_sqrt_round = Math.sqrt(prime).toInt
  var flag = 0
  for(ii <- 2 to prime_sqrt_round){
    if(prime % ii == 0){
      flag = 1
    }
  if(flag == 0){
    sum += prime
    counter += 1
   }
  }
  if(counter == 1000){
    println(sum)
    break
  }
  prime += 2 
}
