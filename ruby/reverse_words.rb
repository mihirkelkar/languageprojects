#!/usr/bin/ruby
fileContent = File.open(ARGV[0], 'r').readlines
fileContent.each do |line|
  word_list = line.chomp.split()
  puts word_list.reverse.join(" ")
end
