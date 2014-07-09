#!/usr/bin/ruby

def make_map(string)
	hash = {}
	string.each_char do |ii|
		begin
			hash[ii] += 1
		rescue 
			hash[ii] = 1
		end
	end
	return hash
end	

def check_anagram(string_one, string_two)
	map_one = make_map(string_one)
	map_two = make_map(string_two)

	if map_one == map_two
		puts "Anagrams Confirmed"
	else
		puts "Not anagrams"
	end		
end	

check_anagram('racecar', 'carrac')
