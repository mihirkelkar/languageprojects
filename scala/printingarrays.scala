object PrintArray{
	def main(args : Array[String]){
		//Using an array in Scala
		var somearray = Array("Hello", "World")
		for(i <- somearray){
			println(i)
		}
		println("----------------------------")
		//Append element to an array
		somearray :+= "America"
		for(i <- somearray){
			println(i)
		}
		println("---------------------------")
		//Prepend element to an array
		somearray +:= "Good morning"
		for(i <- somearray){
			println(i)
		}
	}

}
