term_dict = {}

def calculate_lists(term, index):
  global term_dict
  for ii in term_dict.keys():
    if index != ii:
      term_dict[ii] *= term

def main():
  zero_count = 0
  input_size = input()
  for ii in range(input_size):
    term_dict[ii] = 1
  for ii in range(input_size):
    inputnum = input()
    if inputnum == 0:
      zero_count += 1
    if zero_count > 1:
      continue
    calculate_lists(inputnum, ii)
  for ii in term_dict.values():
    if zero_count > 1:
      print 0
    else:
      print ii

if __name__ == "__main__":
  main()    
