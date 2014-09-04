#!/usr/bin/ruby
fileObj  = File.open(ARGV[0], 'r')
fileList = fileObj.readlines
clean_file_list = []
fileList.each do |line|
  if line == " "
    puts "Line is empty"
  else
    clean_file_list << line
  end
puts clean_file_list  
end
