#The basic idea in this case will be to psuh everythin you encounter onto a stack kind of data structure. 
# So basically if I encounter something that is in the stack, I will pop everything that comes in after its very first appeaence and see if it matches the pattern ahead of it
#If it does not exist. Add it.

def find_most_recent_index(num, list)
  hash = Hash[list.map.with_index.to_a]
  #print hash
  return hash[num]
end

def find_pattern(line)
  pattern_array = []
  pattern_found = 0
  line = line.split()
  line.each do |num|
    if pattern_found == 1
      break
    end
    if pattern_array.include? num
      pattern = []
      index = find_most_recent_index(num, pattern_array) 
      for ii in (index..pattern_array.length - 1)
        pattern << pattern_array[ii]
      end
      #puts pattern
      #puts "======="
      for jj in (0..pattern.length - 1)
        #puts "Matching pattern"
        if pattern[jj] == line[pattern_array.length + jj]
          if jj == pattern.length - 1
            puts pattern.join(' ')
            pattern_found = 1
            break
          end
        else
          break
        end
      end      
    else
      pattern_array << num
    end
  end
end
 
track_list = []
filename = ARGV[0]
fileObj = File.open(filename, 'r')
fileList = fileObj.readlines
fileList.each do |line|
  find_pattern(line)
end

