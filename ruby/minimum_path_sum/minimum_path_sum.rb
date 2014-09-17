"""
The problem is pretty standard, you have a grid. You being from 0, 0 and want to make your way to the n - 1, n - 1 in a n * n grid. You can move only right and bottom.Find the minimum sum along he way from 0,0 to n -1 , n - 1.
THe basic idea in this case is to use dynamic programming. Moving greedily across from 0,0 to n - 1, n- 1 will not give you the correct solution. So move from the bottom. Start from n - 1, n - 1. That number remains contant. Now go to n - 1, n - 2. You can now choose from its right elements only. So you can construct. the bottom most row by simply looking toits right. YOu can construct the right most row by simply looking to its bottom. Now you can construct all other block fo the grid by simply looking down and right and picking the minimum. If you keep doing that, the number picked up at 0,0 will be the minimum path sum
"""

def main()
  File.open(ARGV[0]) do |f|
    until f.eof?
      nextline = f.readline.to_i
      grid = []
      for ii in 1..nextline
        grid << f.readline.strip.split(",").map(&:to_i)
      end
      min_path_sum(grid)
    end
  end
end

def min_path_sum(grid)
  #Building the bottom most row first. R to L
  ii = grid.first.length - 2
  while ii >= 0
    grid[grid.length - 1][ii] += grid[grid.length - 1][ii + 1]
    ii -= 1
  end
  
  #Building the right most row now. Bottom to Top
  ii = grid.length - 2
  while ii >= 0
    grid[ii][grid.first.length - 1] += grid[ii + 1][grid.length - 1]
    ii -= 1
  end
  #building the rest of the grid from bottom to top .right to left. 
  ii = grid.length - 2
  while(ii >= 0)
    jj = grid.first.length - 2
    while(jj >= 0)
      grid[ii][jj] += [grid[ii + 1][jj], grid[ii][jj + 1]].min
      jj -= 1
    end
    ii -= 1
  end
  puts grid[0][0]
end


main() 
