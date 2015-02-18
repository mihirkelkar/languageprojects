def expand(string):
  new_string = ''
  prev_char = ''
  count = 0
  for ii in string:
    if ii.isdigit():
      count = count * 10 + int(ii)
    else:
      new_string += prev_char * count
      prev_char = ii
      count = 0
  new_string += prev_char * count 
  return new_string

print expand('a3b1')    
