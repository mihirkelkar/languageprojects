import util.control.Breaks._
println("This is scala code and you are watching JackAss")
var counter = 0
var prime = 3
var sum = 2
while(true){
  //println("=====================")
  //println("counter is" + counter)
  //println("=====================")
  var prime_sqrt_round = Math.sqrt(prime).toInt
  var flag = 0
  for(ii <- 2 to prime_sqrt_round){
    if(prime % ii == 0){
      flag = 1
    }
  }
  if(flag == 0){
    println("==========")
    println(prime)
    sum += prime
    counter += 1
   }
  if(counter == 1000){
    //println("****************")
    //println("****************")
    //println("counter is 1000")
    //println("****************")
    //println("****************")
    println(sum)
    break
  }
  prime += 2 
}
