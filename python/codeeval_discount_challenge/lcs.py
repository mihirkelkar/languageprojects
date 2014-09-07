def lcs_finder(word_one, word_two):
  grid  = [[0] * (len(word_two) + 1) for ii in range(0, (len(word_one) + 1))]
  for ii in range(1, (len(word_two) + 1)):
    for jj in range(1, (len(word_one) + 1)):
      if word_two[ii - 2] == word_one[jj - 2]:
        grid[ii][jj] = grid[ii - 1][jj - 1] + 1
      else:
        grid[ii][jj] = max(grid[ii][ jj - 1], grid[ii - 1][jj])
  return grid[ii][jj]
def main():
  word_one = "awesome"
  word_two = "aweful"
  lcs_finder(word_one, word_two)
main()
