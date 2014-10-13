#!/usr/bin/python

def possible_decodings(word):
  ret_list = list()
  temp_word = word[0]
  if len(word) > 1:
    for ii in possible_decodings(word[1:]):
      ret_list.append(temp_word + " " + ii)
      ret_list.append(temp_word + ii)
    return ret_list
  else:
    return [word]  

def main():
  word = '1234'
  for ii in possible_decodings(word):
    result  = ""
    flag = 0
    for ii in map(int, ii.split(" ")):
      if ii + 64 > 90 or ii + 64 <= 64 :
        flag = 1
        break
      else:
        result += chr(ii + 64)
    if flag == 0:
      print result 

if __name__ == "__main__":
  main()
