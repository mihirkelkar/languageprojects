#!/usr/bin/python

def all_possible_permutations(word):
  if len(word) == 1:
    return [word]
  else:
    result = list()
    char = word[0]
    perms = all_possible_permutations(word[1:])
    for perm in perms:
      for ii in range(0 ,len(word) + 1):
        result.append(perm[:ii] + char + perm[ii:])
    return result 
    
def well_ordered_words(word):
  temp = all_possible_permutations(word)
  print temp
  for ii in temp:
    flag = 0
    for char in range(0, len(ii) - 1):
      if ord(ii[char].lower()) > ord(ii[char + 1].lower()):
        flag = 1
        break
    if flag == 0:
      print ii

well_ordered_words('aBdel')  
