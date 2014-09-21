def lev(string_one, string_two):
  if len(string_one) == 0:
    return len(string_one)
  elif len(string_two == 0):
    return len(string_two)
  ovrhead = 0 if string_one[-1] == string_two[-1] else 1
  return min(lev(string_one[:-1], string_two) + 1,
             lev(string_one, string_two[:-1]) + 1,
             lev(string_one[:-1], string_two[:-1]) + cost)


