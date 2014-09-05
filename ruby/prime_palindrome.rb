#!/usr/bin/ruby
def prime(number)
  prime = 0
  number_root = Math.sqrt(number).round
  for ii in (2..number_root)
    if number % ii == 0
      prime = 1
      return false
    end
  end
  return true
end

def palindrome(number)
 if number[0] == number[-1]
    if number.length > 2
      palindrome(number[1..-2])
    else
      return true
    end
 else
   return false
 end 
end

biggest_palindrome = 0
ii = 3
while ii <= 1000
  if prime(ii)
    if palindrome(ii.to_s)
      if ii > biggest_palindrome
        biggest_palindrome = ii
      end
    end
  end
  ii += 2
end
puts biggest_palindrome
