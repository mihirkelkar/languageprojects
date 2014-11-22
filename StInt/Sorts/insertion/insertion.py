def insertion(list):
  for ii in range(1, len(list)):
    jj = ii - 1
    key = list[ii]
    while jj >= 0 and list[jj] > list[ii]:
      list[jj + 1] = list[jj]
      jj -= 1
    list[jj + 1] = key
  return list

def main():
  print insertion([3, 1, 4, 8, 5])

if __name__ == "__main__":
  main()
