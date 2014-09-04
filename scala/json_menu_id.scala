import scala.util.matching.Regex
import scala.io.Source
var filecontent = io.Source.fromFile(args(0)).getLines.toList
var clean_content = List[String]()
for(line <- filecontent){
  clean_content ::= line
}
println(clean_content)
var reverse = clean_content.reverse
println(reverse)
var pattern = new Regex("(\\d+)")
for(line <- filecontent){
  var iterator = (pattern findAllIn line)
  var sum = 0
  while (iterator.hasNext){
    sum += iterator.next().toInt
  }
  println(sum)
}
