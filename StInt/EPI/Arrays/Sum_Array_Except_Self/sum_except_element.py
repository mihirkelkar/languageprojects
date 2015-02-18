def sum_except(array):
  left_array = [0]
  right_array = [0]
  temp = 0
  for ii in range(1, len(array)):
    temp += array[ii - 1]
    left_array.append(temp)
  temp = 0
  for ii in range(len(array) - 2, -1, -1):
    temp += array[ii + 1]
    right_array.append(temp)
  right_array.reverse()
  print array
  print "Answers Coming Up Bitches"
  for ii in range(0, len(array)):
    print left_array[ii] + right_array[ii]
    print " - - " * 10
def main():
  sum_except([1, 2, 3, 4])

main()
