#!/usr/bin/python
NUM_LISTS = ['1']
def generate_n_binaries(counter):
  while counter > 0:
    temp = NUM_LISTS.pop(0)
    print temp
    NUM_LISTS.append(temp + '1')
    NUM_LISTS.append(temp + '0')
    counter -= 1

def main():
  generate_n_binaries(10)

if __name__ == "__main__":
  main()
