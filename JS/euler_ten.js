function find_if_prime(number){
  for(var i = 2; i <= Math.round(Math.sqrt(number)); i++){
    if(number % i == 0){
      return false;
    }
  }
  return true;
}
prime_numbers_sum = 2;
for(var i = 3; i < 2000000; i+= 2){
  if(find_if_prime(i)){
    prime_numbers_sum += i;
  }
}

debug(prime_numbers_sum);
