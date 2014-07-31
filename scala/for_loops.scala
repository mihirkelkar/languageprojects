//Using the foreach loop in scala using function literals
args.foreach((arg:String) => println(arg))

println("----------------------")

for (arg <- args){
	print(arg)
        print(" ")
}
println()
