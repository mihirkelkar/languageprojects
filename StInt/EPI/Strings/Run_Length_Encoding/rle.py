#!/usr/bin/python

def rl_encoder(string):
  count = 1
  new_string = ""
  for ii in range(1, len(string)):
    if string[ii] == string[ii - 1]:
      count += 1
    else:
     new_string += str(count)
     new_string += string[ii - 1]
     count = 1
  new_string += str(count)
  new_string += string[ii]
  return new_string


def rl_decoder(en_str):
  count = 0
  dec_str = ""
  for ii in en_str:
    if str.isdigit(ii):
      count = count * 10 + int(ii)
    else:
      new_str = count * ii
      dec_str += new_str
      count = 0
  return dec_str
    

def main():
  temp =  rl_encoder('awesome')
  print temp
  print "--" * 10
  print rl_decoder(temp)
  print "--" * 10

main()
