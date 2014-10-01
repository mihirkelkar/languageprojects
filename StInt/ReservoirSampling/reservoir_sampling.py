#!/usr/bin/python
import random

SAMPLE_COUNT = 10
RANGER = range(random.randint(1, 100), random.randint(100, 10000))

def reservoir_sampling():
  result_list = list()
  for ii in range(len(RANGER)):
    if ii < SAMPLE_COUNT:
      result_list.append(RANGER[ii])
    else:
      number = random.randint(0, ii):
        if number < SAMPLE_COUNT:
          result_list[SAMPLE_COUNT] = RANGER[number]
  return result_list

      
