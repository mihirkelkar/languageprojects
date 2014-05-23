import scala.collection.mutable.ListBuffer

def luhns(creditcard : String) = {
	var creditcardeven = new ListBuffer[Int]
	var creditcardodd  = new ListBuffer[Int]
	println(creditcard)
	for(i <- 0 to creditcard.length - 1){
		if(i % 2 == 0)
			 creditcard(i) +: creditcardeven
		else
			 creditcard(i) +: creditcardodd
	}

	println(creditcardeven)
	println("-----------------------------")
	println(creditcardodd)
}

luhns("12345")
