
object Main{
  def main(args: Array[String]){
    val num_array = io.Source.fromFile(args(0)).getLines
    for(ii <- num_array){
      var numbers = ii.split(":")(0).split(" ").map(_.toInt).toList
      numbers.foreach(println)
      println("==============")
      if(ii.split(":")(1).contains(",")){
        val ranges = ii.split(":")(1).split(",")
        for(range_number <- ranges){
          val range_numbers = range_number.split("-")
          val first = range_numbers(0).replaceAll(" ","").toInt
          val second = range_numbers(1).replaceAll(" ","").toInt
          val first_elem = numbers(first)
          val second_elem = numbers(second)
          
        }
      }
      else{
        val range_numbers = ii.split(":")(1).split("-")
        val first = range_numbers(0).replaceAll(" ","").toInt
        val second = range_numbers(1).replaceAll(" ","").toInt
        val first_elem = numbers(first)
        val second_elem = numbers(second)
        println(numbers.updated(first, second_elem).updated(second, first_elem).mkString(" "))
      }
    }
  }
}
