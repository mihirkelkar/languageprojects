def check_anagram(word_one, word_two):
  hash_map = {}
  for ii in word_one:
    try:
      hash_map[ii] += 1
    except:
      hash_map[ii] = 1
  for ii in word_two:
    try:
      hash_map[ii] -= 1
    except:
      print "Not anagrams"
      return
  if sum(hash_map.values()) != 0:
    print "Not anagrams"
    return
  else:
    print "Anagrams"
    return 

check_anagram("mihir", 'erihim')
