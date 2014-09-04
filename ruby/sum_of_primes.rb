#!/usr/bin/ruby
count_primes = 1
sum_prime = 2
count = 3
while count_primes < 1000
  flag = 1
  for ii in 2..Math.sqrt(count).round
    if count % ii == 0
      flag = 0
      break
    end
  end
  if flag == 1
      #puts count
      sum_prime += count
      count_primes += 1
  end
  count += 2
end
#puts count_primes
puts sum_prime
