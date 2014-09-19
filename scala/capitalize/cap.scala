object Main{
  def main(args: Array[String]){
    val fileContent = io.Source.fromFile(args(0)).getLines.toArray
    for(ii <- fileContent){
      val content  = ii.split(" ").map(_.capitalize)
      println(content.mkString(" "))
    }
  }
}
