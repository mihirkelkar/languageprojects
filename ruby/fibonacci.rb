def fibo(number)
	if number == 0 or number == 1
		return number
	else
		return fibo(number - 1) + fibo(number - 2)
	end

end

puts "Enter the number till which you want the fibonacci series calculated"
puts fibo(gets.chomp.to_i)
