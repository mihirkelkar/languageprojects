def print_matrix_clockwise(matrix):
  top = 0
  down = len(matrix) - 1
  left = 0
  right = len(matrix[0]) - 1
  while(True):
    if left > right:
      break
    else:
      for ii in range(left, right + 1):
        print matrix[top][ii],
      top += 1
    if top > down:
      break
    else:
      for ii in range(top, down + 1):
        print matrix[ii][right],
      right -= 1
    if right < left:
      break
    else:
      for ii in range(right, left - 1, -1):
        print matrix[down][ii],
      down -= 1
    if down < top:
      break
    else:
      for ii in range(down, top - 1, -1):
        print matrix[ii][left],
      left += 1

def print_matrix_anti(matrix):
  top = 0
  down = len(matrix) - 1
  left = 0
  right = len(matrix[0]) - 1
  while(True):
    if left > right:
      break
    else:
      for ii in range(right, left - 1, -1):
        print matrix[top][ii] 
      top += 1
    if top > down:
      break
    else:
      for ii in range(top, down + 1):
        print matrix[ii][left] 
      left += 1
    if left > right:
      break
    else:
      for ii in range(left, right + 1):
        print matrix[down][ii]  
      down -= 1
    if down < top:
      break
    else:
      for ii in range(down, top - 1, -1):
        print matrix[ii][right]
      right -= 1  

matrix = [[1, 2, 3, 4],[2, 4, 9, 5], [9, 8, 7, 6]] 
print_matrix_clockwise(matrix) 
print '- - - - - - - - -'
print_matrix_anti(matrix)
