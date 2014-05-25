puts("Enter your text")
text = gets.chomp.downcase
puts("Enter your shift")
shift = gets.chomp.to_i
decrpyt_text = ""
text.split("").each do |i|
	temp = i.ord + shift % 26
	if temp > 'z'.ord
		temp = temp % 'z'.ord
		temp = 'a'.ord + temp - 1
	end
	puts temp.chr
end
