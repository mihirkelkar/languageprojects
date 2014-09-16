/*The sum is to determine the number of ways you can climb a particular number
of stairs given that you can take only 1 stair or 2 stairs at a time. The recursive solution is to return 1 way to climb the stairs if there is only 1 stairs, there are 2 ways to climb the stairs if there are 2 starits. which is 1 + 1 and 2
. So basically the idea is to climb 1 step and then call the function again to take care of the n - 1 remaining steps. Similarly, you can climb 2 steps and then call the function again to take care of the remaining n - 2 steps
*/ 
val num_array = io.Source.fromFile(args(0)).getLines.toArray.map(_.toInt)
for(ii <- num_array){
  println(calculate_stairs(ii))
}
def calculate_stairs(num_stairs: Int) : Int = {
  if(num_stairs == 1){
    return 1
  }
  if(num_stairs == 2){
    return 2
  }
  return calculate_stairs(num_stairs - 1) + calculate_stairs(num_stairs - 2)
}


