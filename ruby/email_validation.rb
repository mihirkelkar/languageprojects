def validate_email(line)
  if /[\w\d]+@[\w\d]+\.[\w]+/.match(line).to_s == line
    return true
  else
    return false
  end
end

fileContent = File.open(ARGV[0], 'r').readlines
fileContent.each do |line|
  if line != nil
    puts validate_email(line.chomp)
  end
end
