//Find prime factors of a number

function prime_factors(number){
  primefactors = [];
  var d = 2;
  while(d * d <= number){
    while(number % d == 0){
          if(primefactors.indexOf(d) == -1){
            primefactors.push(d);
	  }
          number = number  / d;
	}
    d += 1;
  }
  if(number > 1){
    primefactors.push(number);
  }
  return primefactors;
}

function main(){
  main_numbers = []
  for(var i = 1; i < 21; i++){
    var temp = prime_factors(i);
    for(j = 0; j < temp.length; j++){
      if(main_numbers.indexOf(temp[j]) == -1){
        main_numbers.push(temp[j]);
      }
    }
  }
  var product = 1;
  for(i = 0; i < main_numbers.length; i++){
    product = product  * main_numbers[i];
  }
  debug(product);
}

main()
