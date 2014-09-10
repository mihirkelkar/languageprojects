fileContent = File.open(ARGV[0]).readlines
fileContent.each do |line|
  line = line.chomp
  line.each_char do |char|
    if line.count(char) > 1
      next
    elsif line.count(char) == 1
      puts char
      break
    end
  end
end
