#!/usr/bin/ruby

def check_unique(strings)
	hash_map = {}
	strings.each_char do |i|
		begin
			entry = hash_map[i]
			return false
		rescue 
			hash_map[i] = 1		
		end
	end	
	return true
end	

if check_unique('mihir')
	puts "All charecters unique"
else
	puts "String contains repeated characters"	
end	