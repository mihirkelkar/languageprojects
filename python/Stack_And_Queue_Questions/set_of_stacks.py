"""
Rolling Stack Implementation. After a Stack overflows, implement a new stack and keep adding elements to it. Make the whole thing work seamlessly like a single stack


"""

from stack import *

class SetOfStacks(object):
  def __init__(self, max_el):
    self.set_of_stacks = list()
    self.max_el = max_el

  def set_push(self, value):
    if not self.set_of_stacks:
      self.set_of_stacks.append(Stack())
    if self.set_of_stacks[0].count >= self.max_el:
      self.set_of_stacks.insert(0, Stack())
    self.set_of_stacks[0].push(value)

  def set_pop(self):
    if not self.set_of_stacks:
      return None
    if self.set_of_stacks[0].top == None:
      self.set_of_stacks = self.set_of_stacks[1:]
    self.set_of_stacks[0].pop()

def main():
  dishStack = SetOfStacks(10)
  for ii in range(1, 20):
    dishStack.set_push(ii) 
  dishStack.set_pop()
  for st in dishStack.set_of_stacks:
    print st.printStack()
    print "++++++++++++++++++"
    print "++++++++++++++++++"

if __name__ == "__main__":
  main()     
