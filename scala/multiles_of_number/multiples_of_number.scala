object Main{
  def main(args:Array[String]){
    val num_array = io.Source.fromFile(args(0)).getLines
    for(ii <- num_array){
      var temp = ii.split(",").map(_.toInt)
      find_multiple(temp(0), temp(1))
    }
  }

  def find_multiple(bigger_than:Int, number: Int) : Boolean = {
    var counter = 1
    while(true){
      if(number * counter < bigger_than){
        counter += 1
      }
      else{
        println(number * counter)
        return true
      }
    }
    error("Some Unit expected madness in scala forces me to do this. Every fucking time")
  }
}
