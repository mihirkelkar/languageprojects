"""
Design a code for the secret santa game where one person buys a gift for only one person in the office such that evey one gets a gift. 
"""
import random

people = [['lily', 0], ['barney', 0], ['ted', 0], ['robin', 0], ['marshall',0]]

buy_for = [ii[0] for ii in people]

for ii in range(len(people)):
  while True:
    temp = random.choice(range(len(buy_for)))
    if buy_for[temp] == people[ii][0]:
      continue
    else:
      people[ii][1] = buy_for[temp]
      buy_for.pop(temp)
      break
print people
