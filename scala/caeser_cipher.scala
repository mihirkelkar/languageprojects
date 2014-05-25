println("Enter text to be encrypted")
var text = readLine().toLowerCase
println("Enter shifting number")
var shift = readInt()
//println(text)
//println(shift)
var cipher = ""
for(x <- 0 to text.length - 1){
	var temp = text(x).toInt + shift % 26
	if(temp > 'z'.toInt){
		temp = temp % 'z'.toInt
		temp = 'a'.toInt + temp - 1
	}
	cipher += temp.toChar
}
println(cipher)
