import scala.collection.mutable.ListBuffer

def calc_number_of_paths(grid: ListBuffer[ListBuffer[String]], x:Int, y:Int) : Int = {
  if(grid(x)(y) == "0"){
    return 0
  }
  if(x == 3 && y == 3){
    return 1
  }
  var count = 0
  grid(x)(y) = "0"
  if(x > 0){
    count += calc_number_of_paths(grid, x - 1, y)
  }
  if(x < 3){
    count += calc_number_of_paths(grid, x + 1, y)
  }
  if(y > 0){
    count += calc_number_of_paths(grid, x, y - 1)
  }
  if(y < 3){
    count += calc_number_of_paths(grid, x, y + 1)
  }
  grid(x)(y) = "1"
  return count
}

var grid = ListBuffer[ListBuffer[String]]()
for(ii <- 0 to 3){
  grid += ListBuffer("1", "1", "1", "1")
}

println(calc_number_of_paths(grid ,0, 0))
