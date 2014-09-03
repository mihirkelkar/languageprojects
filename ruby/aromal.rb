#!/usr/bin/ruby
def find_decimal_value(line)
  #puts line
  sum = 0
  roman = {
  "I" => 1,
  "V" => 5,
  "X" => 10,
  "L" => 50,
  "C" => 100,
  "D" => 500,
  "M" => 1000
  }
  #Make groups of two from the string that was passed to you
  grps_two = line.scan /.{1,2}/
  grps_two = grps_two.reverse
  #puts grps_two
  #puts "**********"
  for ii in (0..grps_two.length - 2)
    if roman[grps_two[ii].split("")[1]] > roman[grps_two[ii + 1].split("")[1]]
      sum -= grps_two[ii].split("")[0].to_i * roman[grps_two[ii].split("")[1]]
    else
      sum += grps_two[ii].split("")[0].to_i * roman[grps_two[ii].split("")[1]] 
    end
  end
  sum += grps_two[grps_two.length - 1].split("")[0].to_i * roman[grps_two[grps_two.length - 1].split("")[1]] 
  puts sum
end

fileobj  = File.open(ARGV[0], 'r')
file_content = fileobj.readlines
file_content.each do |line|
  find_decimal_value(line.chomp)
end

