#!/usr/bin/ruby
fileContent = open(ARGV[0], 'r').readlines
fileContent.each do |line|
  reverse_temp = line.split().reverse
  join_list = []
  for ii in (0..reverse_temp.length - 1)
    if ii % 2 == 0
      join_list << reverse_temp[ii].to_s
    end
  end
  puts join_list.join(" ")
end
