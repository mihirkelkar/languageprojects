#!/usr/bin/ruby
def find_primes_till(number)
  prime_list = []
  for ii in (2..number)
    prime = 1
    for jj in (2..Math.sqrt(ii).round)
      if ii % jj == 0
        prime = 0
        break
      end
    end
    if prime == 1
      prime_list << ii
    end
  end
  puts prime_list.join(",")
end

fileContent = File.open(ARGV[0], 'r').readlines
fileContent.each do |lines|
  number = lines.chomp.to_i
  find_primes_till(number - 1)
end
