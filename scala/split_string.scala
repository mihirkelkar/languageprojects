//Splitting a string into an array and then printing it by iterating through it
var string = "Mihir Kelkar"
var string_array = string.split(" ")
string_array.foreach(s => print(s))

//Split a string into chars and printing it
string = "Starwars"
string_array = string.split("")
string_array.foreach(s => println(s))

//Using sets and maps in scala
var capital = Map("California" -> "Sacramento", "Oregon" -> "Portland")
println(capital("California"))

//Using a set in Scala
var jetSet = Set("Boeing", "Airbus", "Eurofighter Typhoon")
jetSet += "F16"
println(jetSet.contains("Cessna"))
println(jetSet)
