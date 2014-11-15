def permutations(word):
  if len(word) == 1:
    return [word]
  else:
    char = word[0]
    result = list()
    perm_list = permutations(word[1:])
    for perm in perm_list:
      for ii in range(0, len(perm) + 1):
        result.append(perm[:ii] + char + perm[ii:])
    return result

print permutations('abc')
