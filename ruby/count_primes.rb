def count_primes(num_one, num_two)
  prime_counter = 0
  for ii in (num_one..num_two)
    if is_prime(ii)
      prime_counter += 1
    end
  end
  puts prime_counter
end

def is_prime(ii)
  if ii % 2 == 0 && ii != 2
    return false
  end
  for num in (2..Math.sqrt(ii).round.to_i)
    if ii % num == 0
      return false
    end
  end
  return true
end

fileContent = File.open(ARGV[0], 'r').readlines
fileContent.each do |lines|
  lines = lines.chomp.split(',')
  count_primes(lines[0].to_i, lines[1].to_i)
end 
