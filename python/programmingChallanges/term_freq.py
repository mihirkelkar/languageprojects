term_dict = {}

def term_freq(term):
  global term_dict
  try:
    term_dict[term] += 1
  except:
    term_dict[term] = 1

def print_k(k):
  global term_dict
  freq_count = sorted(term_dict.items(), key = lambda ii: (-ii[1], ii[0]))
  for ii in range(k):
    print freq_count[ii][0]

def main():
  size = input()
  for ii in range(size):
    term_freq(raw_input().strip())
  print_k(input())

main()
