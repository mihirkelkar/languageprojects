"""
A robot is located at the top left corner of the 4 * 4 grid. The robot can ake left, right, top, botom movements. The robot is trying to reach the bottom right corners. You however cannot visit the same spot twice. 
"""

def count_number_of_paths(grid, x, y)
  if grid[x][y] == 0
    return 0
  end
  if x == 3 && y == 3
    return 1
  end
  grid[x][y] = 0
  count = 0
  if x < 3
    count += count_number_of_paths(grid, x + 1, y)
  end
  if x > 0
    count += count_number_of_paths(grid, x - 1, y)
  end
  if y < 3
    count += count_number_of_paths(grid, x, y + 1)
  end
  if y > 0
    count += count_number_of_paths(grid, x, y - 1)
  end
  grid[x][y] = nil
  return count
end

grid = (1..4).map {Array.new 4}
puts count_number_of_paths(grid, 0, 0)
