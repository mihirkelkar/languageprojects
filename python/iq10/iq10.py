#!/usr/bin/python
FINAL_NUM_LEN = 7
letter = {'1': '1', '2':'ABC', '3':'DEF', '4':'GHI', '5':'JKL', '6':'MNO', '7':'PRS', '8':'TUV', '9':'WXY'}
fp = open("words", "w")
def num_toStr(cur_digit, chars = ''):
  global FINAL_NUM_LEN
  global letter
  global number
  global fp
  if cur_digit == FINAL_NUM_LEN - 1:
    letters = letter[number[cur_digit]]
    for i in letters:
      fp.write(chars + i + "\n")
  else:
    letters = letter[number[cur_digit]]
    for i in letters:
      num_toStr(cur_digit + 1, chars + i)


def main():
  global number
  global fp
  while(True):
    number  = raw_input("Enter your 7 digit phone number").replace("-","")
    if len(number) == 7:    
      break
  num_toStr(0)
  fp.close()

if __name__ == "__main__":
  main()
    		
