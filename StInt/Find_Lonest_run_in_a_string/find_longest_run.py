#!/usr/bin/python

def find_longest_run(string):
  run = string[0]
  longest_run_char = run
  longest_run_count = 1
  count = 1
  for ii in range(1, len(string)):
    if string[ii] == run:
      count += 1
      if count >= longest_run_count:
        longest_run_count = count
        longest_run_char = string[ii]
    else:
      run = string[ii]
      count = 1
  return longest_run_char * longest_run_count

def main():
  print find_longest_run('aaaabbccdd')

if __name__ == "__main__":
  main()
  

