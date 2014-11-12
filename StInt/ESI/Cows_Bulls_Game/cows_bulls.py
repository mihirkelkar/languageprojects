def cows_bulls(word_one, word_two):
  cows = 0
  bulls = 0
  first_word_hash = {}
  for ii in range(0, len(word_one)):
    try:
      first_word_hash[word_one[ii]].append(ii)
    except:
      first_word_hash[word_one[ii]] = [ii]
  print first_word_hash
  for ii in range(0, len(word_two)):
    try:
      print word_two[ii]
      temp = first_word_hash[word_two[ii]]
      if ii in temp:
        bulls += 1
      elif ii not in temp:
        cows += 1
    except:
      pass
  print "Cows are %s"%cows
  print "Bulls are %s"%bulls

cows_bulls('picture', 'epic')
cows_bulls('mihir', 'wihir')
