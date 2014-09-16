require 'set'
fileContent = File.open(ARGV[0], "r").readlines
fileContent.each do |lines|
  missing = []
  lines = lines.chomp.downcase.gsub! " ",""
  if lines != nil
    lines =  lines.chars.sort.join
  else
    lines = ""
  end
  for ii in (97..122)
    if lines.include? ii.chr
      next
    else
      missing << ii.chr
    end
  end
  if missing.length == 0
    puts "NULL"
  else
    puts missing.join
  end
end
