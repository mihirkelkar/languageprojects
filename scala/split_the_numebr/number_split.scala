object Main{
  def main(args: Array[String]){
    val num_array = io.Source.fromFile(args(0)).getLines
    for(ii <- num_array){
      val line = ii.split(" ")
      println(split_number(line(0), line(1)))
    }
  }

  def split_number(number: String, pattern: String): Int = {
    var index = 0
    var sign = ""
    if(pattern.contains("-")){
      index = pattern.indexOfSlice("-")
      sign = "-"
    }
    else{
      index = pattern.indexOfSlice("+")
      sign + "+"
    }
    val Part_one = number.take(index).toInt
    val Part_two = number.drop(index).toInt
    if(sign == "-"){
      return Part_one - Part_two
    }
    else{
      return Part_one + Part_two
    }
  }
}
