=begin
Unit Covertor: (Unit Converter (temp, currency, volume, mass and more) - Converts
various units between one another. The user enters the type of unit
being entered, the type of unit they want to convert to and then
the value. The program will then make the conversion.
=end 

def convert_temperature()
	puts "Enter your input unit\n 1. Farheniet\n 2. Celcius\n"
	unit = gets.chomp.to_i
	puts "Enter your value to be converted"
	value = gets.chomp.to_i
	if unit == 1
		con = ((value - 32) * 5) / 9
		puts 'Converted Values in Celcius is %s' % con
	elsif unit == 2
		con = (value * 9 / 5) + 32
		puts 'Converted Values in Farheniet is %s' %con		
	end
end	

def convert_length()
	puts "Enter your input unit \n1.Meters\n2.Km\n 3.Foot\n4.Miles\n"
	unit = gets.chomp.to_i
	puts "Enter your value to be converted"
	value = gets.chomp.to_i
	puts "Enter the unit to convert to\n1.Meters\n2.Km\n 3.Foot\n4.Miles\n"
	counit = gets.chomp.to_i
	if unit == 1
		meterstd = value
	elsif unit == 2
		meterstd = value * 1000
	elsif unit == 3
		meterstd = value / 3.28
	elsif unit == 4
		meterstd = value * 1609.34
	end

	if counit == 1
			puts meterstd
	elsif counit == 2
		puts meterstd / 1000
	elsif counit == 3
		puts meterstd * 3.28
	elsif counit == 4
		puts meterstd / 1609.34
	end			
																

end

def convert_currency()
	puts "Select your Input Currency\n1.US Dollar\n2.Euro\n3.British
	Pound\n4.Icelandic Krona\n"
	unit = gets.chomp.to_i
	puts "Enter the value "
	value = gets.chomp.to_f
	puts "Select Currency to convert to\n1.US Dollar\n2.Euro\n3.British
	Pound\n4.Icelandic Krona\n"
	counit = gets.chomp.to_i
	if unit == 1
		meterstd = value
	elsif unit == 2
		meterstd = value * 1.36
	elsif unit == 3
		meterstd = value * 1.70
	elsif unit == 4
		meterstd = value * 0.0088
	end

	if counit == 1
			puts meterstd
	elsif counit == 2
		puts meterstd / 1.36
	elsif counit == 3
		puts meterstd /1.70
	elsif counit == 4
		puts meterstd / 0.0088
	end
end	



def main()
	puts "Unit Convertor. 1.Temperrature\n 
		2. Length
		3. Currency"
	choice = gets.chomp.to_i
	if choice == 1
		convert_temperature()
	elsif choice == 2
		convert_length()
	elsif choice == 3
		convert_currency()								
	end

end

main()