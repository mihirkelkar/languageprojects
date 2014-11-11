def find_colorful_number(number):
  result = list()
  mult_hash = {}
  string = str(number)
  for ii in range(1, len(string)):
    jj = 0
    while jj + ii <= len(string):
      result.append(string[jj:jj+ii])
      jj += 1
  for ii in result:
    if len(ii) == 1:
      mult_hash[int(ii)] = True
    else:
      product = 1
      for num in ii:
        product *= int(num)
      try:
        temp = mult_hash[product]
        return False
      except:
        pass
  return True 
  
print find_colorful_number(326)
