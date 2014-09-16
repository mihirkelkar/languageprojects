#!/usr/bin/ruby
fileObj = File.open(ARGV[0], 'r')
fileContent = fileObj.readlines
fileContent.each do |line|
  list_one, list_two = line.chomp.split("|")
  list_one = list_one.split(" ")
  list_two = list_two.split(" ")
  product_list = []
  for ii in (0..(list_one.length - 1))
    product_list << list_one[ii].to_i * list_two[ii].to_i
  end
  puts product_list.join(" ")
end
