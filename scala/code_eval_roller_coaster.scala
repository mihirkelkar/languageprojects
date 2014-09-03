import scala.io.Source
//Accepting Command line arguements in scala is straight forward by args
//Get the filename from the command line, open the file and then read it into 
//a list
var filecontent = io.Source.fromFile(args(0)).getLines.toList
for(line <- filecontent){
  var counter = 0
  var list_roller = List[String]()
  for(char <- line.toLowerCase){
    if(char.toInt >= 97 && char.toInt <= 122){
      if(counter % 2 == 0){
        list_roller ::= char.toString.toUpperCase
        counter+=1
      }
      else{
        list_roller ::= char.toString.toLowerCase
        counter += 1
      }
    }
    else{
      list_roller ::= char.toString
    }
  }
  println(list_roller.reverse.mkString)
}
