#!/usr/bin/ruby

def roller_coaster(line)  
  puts "this is a new roller coaster function"
end

def main()
  filename = File.open("text", "r")
  filename.each_line do |line|
    counter = 0
    roller_text = []
    line.each_char do |char|
      if (97..122).include? char.downcase.ord 
        if counter % 2 == 0
          roller_text << char.upcase
          counter += 1
        else
          roller_text << char.downcase
          counter += 1
        end
      else
        roller_text << char
      end
    end
    puts roller_text.join("")
  end
  filename.close
end

main()
