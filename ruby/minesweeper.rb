# You are given an M*N matrix. Each item in this matrix is either a '*' or a
# '.'. A '*' indicates a mine whereas a '.' does not. The objective of the
# challenge is to output a M*N matrix where each element contains a number
# (except the positions which actually contain a mine which will remain as '*')
# which indicates the number of mines adjacent to it.
def find_mines(grid, column, row)
  num_mines = 0
  for ii in (-1..1)
    for jj in (-1..1)
      row_temp = row + ii
      col_temp = column + jj
      if row_temp < 0 || row_temp >=grid.size || col_temp < 0 || col_temp >= grid[0].length
        next
      else
        if grid[row_temp][col_temp] == "*"
          num_mines += 1
        end
      end  
    end
  end
  return num_mines
end

def run_thru_grid(grid)
  for ii in (0..(grid.size - 1))
    for jj in (0..(grid.first.size - 1))
        if grid[ii][jj] == "."
          grid[ii][jj] = find_mines(grid, ii, jj)
        end
    end
  end
  return grid
end

contentGrid = File.open(ARGV[0]).readlines
contentGrid.each do |lines|
  dimensions, data = lines.strip.split(";")
  row, col = dimensions.split(",").map(&:to_i)
  grid = []
  for ii in (0..(row - 1))
    temp_grid = []
    for jj in (0..(col - 1))
      temp_grid << data[row * ii + jj]   
    end
  grid << temp_grid
  end
  puts run_thru_grid(grid)
end
