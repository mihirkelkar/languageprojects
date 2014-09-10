fileContent = File.open(ARGV[0]).readlines
fileContent.each do |line|
  x,y = line.chomp.split(",")
  y = y.gsub(" ","")
  y.each_char do |char|
    x = x.gsub(char, "")
  end
  puts x
end
