WORD_DICT = {
  '0' : ['0'],
  '1' : ['1'],
  '2' : list('abc'),
  '3' : list('def'),
  '4' : list('ghi'),
  '5' : list('jkl'),
  '6' : list('mno'),
  '7' : list('pqrs'),
  '8' : list('tuv'),
  '9' : list('wxyz')
}


def phone_number(number):
  if len(number) > 1:
    ret_val = phone_number(number[1:])
  elif len(number) == 1:
    ret_val = WORD_DICT[number[0]]
    return ret_val
  result_list = list()
  for ii in WORD_DICT[number[0]]:
    result_list += [ii + jj for jj in ret_val]
  return result_list

def main():
  temp = phone_number('478') 
  print len(temp)
  print temp
if __name__ == "__main__":
  main()
