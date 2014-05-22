#!/usr/bin/ruby
#Credit card validation code in ruby
#Testcase is account number is 79927398713
def luhns(creditcardnumber)
	card_number = creditcardnumber.split("")
	card_number_evens = []
	card_number_odds = []
	card_number.each_with_index do |element, index|
		if index % 2 == 0
			element = element.to_i
			card_number_evens << element
		elsif index % 2 == 1
			element = element.to_i
			card_number_odds << element * 2
		end
	end
	#puts card_number_evens
	#puts "---------------------------"
	#puts card_number_odds
	#puts "---------------------------"
	card_number_odds.each_with_index do |element, index|
		if element > 9
			temparray  = element.to_s.split("")
			temparray.each_with_index do |number, nope|
				temparray[nope] = number.to_i
			end
			card_number_odds[index] = temparray.inject(:+)
			#puts card_number_odds	
			#puts "-------------------"
		end
	end
	final = (card_number_evens.concat(card_number_odds).inject(:+) * 9) % 10
	#puts final
	#puts "-------------------------"
	return final
	
	
end

puts "Enter the credit card number"
card_number = gets.chomp
digit = card_number[-1].to_i
#puts "digit is " , digit
if luhns(card_number[0..-2]) == digit
	puts "Valid"	
else
	puts "Invalid"
end


