"""
The problem here is that given a number n which is the number of stairs, calculate the number of ways you can reach the top given that you can take either 1 step or two steps. 
A probable recursive solution lies in the fact that we can take one step and then figure out how to take the rest of the n - 1 steps, or take two steps and the figure out how to do the rest of the n - 2 steps. 
"""
#The recursive method is a little inefficient. 
#def calculate_ways(number_of_stairs)
#  if number_of_stairs == 1
#    # Climb One step
#    return 1
#  end
#  if number_of_stairs == 2
#    #1+1 steps or 2 steps
#    return 2
#  end
#  return calculate_ways(number_of_stairs-1)+calculate_ways(number_of_stairs-2)
#end

def calculate_ways(num_stairs)
  prev_steps = [1,2]
  count = 0
  while count < num_stairs 
    prev_steps << prev_steps[-1] + prev_steps[-2]
    count += 1
  end
  return prev_steps[num_stairs - 1]
end

def main
  File.open(ARGV[0]).map(&:to_i).each do |number|
    puts calculate_ways(number)
  end
end

main()
