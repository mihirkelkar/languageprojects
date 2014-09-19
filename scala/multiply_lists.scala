import scala.io.Source
var filecontent = io.Source.fromFile(args(0)).getLines.toList
for(line <- filecontent){
  var lister = line.split("|")
  println(lister)
  println(lister)
}

