def pat_match(string, parts, pattern, result = list()):
  if len(result) < parts:
    if string != '':
      for ii in range(0, len(string)):
        pat_match(string[ii + 1:], parts, pattern, result + [string[:ii+1]])
  else:
    flag = 0
    temp = dict(zip(set(pattern), [[] for ii in range(len(set(pattern)))]))
    for ii in range(len(pattern)):
      if temp[pattern[ii]] == []:
        temp[pattern[ii]].append(result[ii])
      else:
        if temp[pattern[ii]][0] != result[ii]:
          flag = 1
          break
    if flag == 0:
      print result       
pat_match('redbluebluered', 4, 'abba')
