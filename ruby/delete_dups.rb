#!/usr/bin/ruby
#Delete all duplicate charecters in a string
def check_dups(string)
	hash_map = {}
	string.each_char do |i|
		begin
			hash_map[i] += 1
		rescue
			hash_map[i] = 1
		end		
	end
	hash_map.each do |key, count|
		if count > 1
			string = string.tr(key, '')		
		end	
	end	
	puts string
end		

check_dups('mihirkelkar')
