function find_triangle_numbers(limit){
  triangle_numbers = [];
  for(var count = 1; count < limit; count++){
    var sum = 0;
    for(var i = 0; i <= count; i++){
        sum += i;
    }
    triangle_numbers.push(sum);
  }
  return triangle_numbers;
}

function find_number_of_factors(number){
  num_divisors = 0
  for(var count = 1; count <= number; count++){
    if(number % count == 0){
      num_divisors++;
    }
  }
  debug(num_divisors);
  if(num_divisors < 100){
    return false;
  }
  else{
    return true;
  }
}

triangle_numbers = find_triangle_numbers(200000);
for(var index = 0; index < triangle_numbers.length; index++){
  if(find_number_of_factors(triangle_numbers[index])){
    break;
    debug(triangle_numbers[index]);
  }
}
