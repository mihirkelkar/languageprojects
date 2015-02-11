#!/usr/bin/python

def sine_print(string):
  middle_buffer = list()
  up_buffer = list()
  down_buffer = list()
  up_flag = True
  for ii in range(len(string)):
    if ii % 2 == 0:
      middle_buffer.append(string[ii])
      up_buffer.append(" ")
      down_buffer.append(" ")
    else:
      if up_flag:
        up_buffer.append(string[ii])
        down_buffer.append(" ")
      elif  not up_flag:
        down_buffer.append(string[ii])
        up_buffer.append(" ")
      up_flag = not up_flag
      middle_buffer.append(" ")
  print "".join(up_buffer)
  print "".join(middle_buffer)
  print "".join(down_buffer)

def main():
  string = "test string"
  string = string.replace(" ","~")
  sine_print(string)
  

if __name__ == "__main__":
  main()
    
