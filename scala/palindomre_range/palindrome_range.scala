import scala.collection.mutable.ListBuffer
import scala.util.control.Breaks._
def is_palindrome(number: String) : Boolean = {
  return if(number.reverse == number) true else false
}

def palindrome_range(left: Int, right: Int): Array[Boolean] = {
  var palindrome_list = ListBuffer[Boolean]()
  for(ii <- left to right){
    palindrome_list += is_palindrome(ii.toString)
  }
  //println("Returned range array")
  return palindrome_list.toArray
}

def count_palindromes(palindrome_list: Array[Boolean]): Int = {
  var result = 0
  //println("Entered count palindrome")
  for(end <- 1 to palindrome_list.length + 1){
    breakable{for (start <- 0 to palindrome_list.length){
      if(start + end > palindrome_list.length){
          break
        }
      var even_count = 0
      for(ii <- start to start + end - 1){
          if(palindrome_list(ii) == true){
            even_count += 1
          }
        }
      if (even_count % 2 == 0){
        result += 1
      }
      }
    }
  }
  //println("Returned the integer")
  return result
}

val test_cases = io.Source.fromFile(args(0)).getLines.toArray
for(ii <- test_cases){
  var temp = ii.split(" ").toArray.map(_.toInt)
  //println(temp(0))
  //println(temp(1))
  println(count_palindromes(palindrome_range(temp(0), temp(1))))
}
