class Circbuffer(object):
  def __init__(self, size):
    self.size = size
    self.values = list()
    self.current_mod = 0    

  def append(self, values):
    cur_mod = 0
    for ii in values:
      if len(self.values) < self.size:
        self.values.append(ii)
      else:
        self.values[cur_mod] = ii
        cur_mod += 1
        cur_mod = cur_mod % self.size
        self.current_mod = cur_mod

  def remove(self, num):
    if self.values:
      for ii in range(num):
        if self.current_mod <= len(self.values):
          self.values.pop(self.current_mod)
        else:
          self.current_mod = 0
          if self.values:
            self.values.pop(0)

  def list(self):
    #listing the elements in the order of inserting time
    for ii in range(self.current_mod, len(self.values)):
      print self.values[ii]
    for ii in range(0, self.current_mod):
      print self.vales[ii]

def main():
  circbuffer = Circbuffer(input())
  while True:
    choice = raw_input().strip()
    if choice == 'L' or choice == 'Q':
      act = choice
    else:
      act, num = list(choice.replace(' ',''))
    if act == 'A':
      temp_list = list()
      for ii in range(int(num)):
        temp_list.append(raw_input().strip())
      circbuffer.append(temp_list)  
    elif act == 'R':
      circbuffer.remove(int(num))
    elif act == 'L':
      circbuffer.list()
    elif act == 'Q':
      break

if __name__ == "__main__":
  main()
