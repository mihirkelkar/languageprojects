def permutations(word):
  print '==========='
  print word
  res = list()
  if len(word) == 1:
    res.append(word)
  else:
    for ii in range(0, len(word)):
      temp = word[ii]
      te = word[:ii] + word[ii + 1:] 
      for el in permutations(te):
        res.append(temp + el)
      print res
  return res


def main():
  print permutations('abc')

if __name__ == "__main__":
  main()
