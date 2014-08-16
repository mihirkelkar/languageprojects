import scala.util.control.Breaks._
var string = "PAwesome"
val vowel = "aeiou"
var list = string.toList
/*for (i <- 0 to list.length - 1){
	println(vowel.contains(list(i).toString.toLowerCase))
}
*/
if(vowel.contains(list.head.toString.toLowerCase)){
	println(list.mkString("").toLowerCase + "way")
}
else{
  var length = list.length
  var appendList = List[String]()
  for(i <- 0 to list.length - 1){
		if(vowel.contains(list(i).toString.toLowerCase)){
			//println("Entered the if case")
			list = list.drop(i)
			//println(list)
			//println(appendList)
                        var answer = list.mkString("").toLowerCase + appendList.mkString("") + "ay"
			println(answer)
			break
		}
		else{
			//println("Entered the else case")
			//Scala lists are not mutable. So we just overwrite them
			appendList = list(i).toString :: appendList
			//println(appendList)
			appendList.foreach(arg => println(arg))
		}	
	}
        //println(answer)
}
