#!/usr/bin/python
#Code to sort a stack using another stack. 
from stack import *

def sort(stack):
  new_stack = Stack()
  while stack.top != None:
    value = stack.pop()
    while new_stack.top != None and new_stack.top.value > value:
      stack.push(new_stack.pop())
    new_stack.push(value)
  return new_stack
