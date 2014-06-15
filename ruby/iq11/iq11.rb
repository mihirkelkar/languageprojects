#!/usr/bin/ruby

def advanced_fizz_buzz(a, b)
	a = a.to_i
	b = b.to_i
	fizz_count = buzz_count = fizzbuzz_count = 0
	while a <= b
		if a % 3 == 0
			if a % 5 == 0
				fizzbuzz_count += 1
			else
				fizz_count += 1	
			end

		elsif a % 5 == 0
			buzz_count += 1
		end	
	a += 1	
	end
	return fizz_count, buzz_count, fizzbuzz_count
end	

def main()
	temp = advanced_fizz_buzz(2, 6)
	puts temp
end	

main()