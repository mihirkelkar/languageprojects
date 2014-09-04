#!/usr/bin/ruby
filename = ARGV[0]
fileObj = File.open(filename, 'r')
fileList = fileObj.readlines
number = fileList[0].chomp.to_i
fileList = fileList[1..fileList.length]
fileList = fileList.sort_by{|x| x.length}
ii = 0
while ii < number
  puts(fileList[-1 - ii])
  ii += 1
end
