#!/usr/bin/python

def longest_palindrome_substring(word_one):
  table = [[False] * len(word_one) for ii in range(len(word_one))]
  
  #I will go ahead and mark all substrings of length one to be palindromes
  for ii in range(len(word_one)):
    table[ii][ii] = True
    maxlength = 1
  start = 0
  #Now looking for substrings which are of length two. 
  for ii in range(0, len(word_one) - 1):
    if word_one[ii] == word_one[ii + 1]:
      word_one[ii][ii + 1] = True
      start = ii
      max_length = 2

  #Now checking for palindromic substrings of length 3 and greater. 
  counter = 3
  while counter <= len(word_one):
    for ii in range(0, len(word_one) - counter):
      jj = ii + counter - 1
      if table[ii + 1][jj - 1] and word_one[ii] == word_one[jj]:
        table[ii][jj] = True
        if counter > maxlength:
          max_length = k


