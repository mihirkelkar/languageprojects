import random

#Representing a stack using lists. 
class Stack(object):
  def __init__(self):
    self.container = list()
  
  def push(self, value):
    self.container.append(value)

  def pop(self):
    if self.container:
      return self.container.pop()
    else:
      return None

  def size(self):
    if self.container:
      return True
    return False


def stack_sort(stack_one):
  stack_two = Stack()
  while stack_one.size():
    value_temp = stack_one.pop()
    while stack_two.size() and stack_two.container[-1] > value_temp:
      stack_one.push(stack_two.pop())
    stack_two.push(value_temp)
  return stack_two 

stack_new = Stack()
for ii in range(1, 16):
  stack_new.push(random.randint(1, 1000))
print stack_new.container
temp = stack_sort(stack_new)
print temp.container 
