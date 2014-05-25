def palindrome(string)
	if string.length > 1
		if string[0] == string[-1]
			palindrome(string[1..-2])
		else
			puts "Not a palindrome"
		end
	else
		puts "Palindrome"

	end
end


puts "Enter your text string"
string = gets.chomp.downcase.gsub(" ","")
puts string
palindrome(string)
