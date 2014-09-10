#!/usr/bin/ruby
def calculate_till_palindrome(line)
  reverse = line.reverse.to_i
  line = line.to_i
  counter = 0
  while true
    counter += 1
    line = line + reverse
    if line.to_s == line.to_s.reverse
      puts [counter, line].join(" ")
      break
    else
      reverse = line.to_s.reverse.to_i
    end
  end
end

fileContent = File.open(ARGV[0], 'r').readlines
fileContent.each do |line|
  line = line.chomp
  #puts line
  calculate_till_palindrome(line)
end
