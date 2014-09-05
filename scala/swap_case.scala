import scala.io.Source
//Opening the file and then reading it
object SwapCase{
  def main(args : Array[String]){
  var filecontent = io.Source.fromFile(args(0)).getLines.toList
  //iterating through the entire list
  for(line <- filecontent){
    var list = List[String]()
    //Iterating through each char in any given line
    for(char <- line){
      if(char.toInt >= 97 && char.toInt <= 122){
      //If the given char is small case, make it upper case and add it to string
        list ::= char.toString.toUpperCase
      }
      else if(char.toInt >= 65 && char.toInt <= 90){
      //If the char is upper case, make it lower case and add it to the string
        list ::= char.toString.toLowerCase
      }
      else{
        list ::= char.toString
      }
    }
    println(list.reverse.mkString)
  }
}
}
