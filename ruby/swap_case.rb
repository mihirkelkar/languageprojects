#!/usr/bin/ruby
fileContent = open(ARGV[0], "r").readlines
fileContent.each do |line|
  char_string = ""
  line.each_char do |char|
    if (97..122).include? char.ord
      char_string += char.upcase
    elsif (65..90).include? char.ord
      char_string += char.downcase
    else
      char_string += char
    end
  end
  puts char_string
end

