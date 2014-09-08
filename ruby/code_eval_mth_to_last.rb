#!/usr/bin/ruby
fileContent = File.open(ARGV[0], 'r').readlines
fileContent.each do |line|
  line = line.chomp.split
  number = line[-1].to_i
  line =  line[0..-2]
  if number <= line.length
    puts line.reverse[number - 1]
  end
end
