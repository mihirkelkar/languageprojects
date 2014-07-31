val greetStrings = new Array[String](3)
greetStrings(0) = "Hello "
greetStrings(1) = "Scala "
greetStrings(2) = "Wazzup?\n"

for(i <- 0 to 2)
  print(greetStrings(i))

