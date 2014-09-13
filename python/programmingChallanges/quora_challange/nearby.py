#!/usr/bin/python
import math
def calc_queries(qu, topics, questions):
  type, number, x_cord, y_cord = qu.strip().split(" ")
  x_cord = float(x_cord)
  y_cord = float(y_cord)
  number = int(number)
  min_distance_list = list()
  for ii in topics.items():
    min_distance_list.append((ii[0], round(math.sqrt((x_cord - ii[1][0]) ** 2 + (y_cord - ii[1][1]) ** 2), 3)))
    min_distance_list = sorted(min_distance_list, key = lambda ii: (ii[1]-int(ii[0])))
  if type == 't':
    print "Entered here dude"
    print [ii[0] for ii in min_distance_list][:number]
  elif type == 'q':
    needed_num = []
    for ii in range(0, len(min_distance_list)):
      cur_topic = min_distance_list[ii][0]
      temp_carry = list()
      for ii in questions.items():
        if cur_topic in ii[1]:
          if ii[0] not in needed_num:
            temp_carry.append(ii[0])
        print temp_carry
        needed_num += sorted(temp_carry, reverse = True)
        #print "added to needed num"
    print needed_num
          
    
      
def main():
  num_topics, num_quest, num_queries = raw_input().strip().split(" ")
  #print num_topics
  #print num_quest
  #print num_queries
  topics = {}
  for tt in range(int(num_topics)):
    #print "This is topic number %s" %(tt + 1)
    id, x_cord, y_cord = raw_input().strip().split(" ")
    topics[id] = [float(x_cord), float(y_cord)]
  questions = {}
  for qq in range(int(num_quest)):
    #print "This is question number %s" %(qq + 1)
    question_str = raw_input().strip().split(" ")
    if question_str[1] == "0":
      #print "Not added to question dict"
      pass
    else:
      questions[question_str[0]] = question_str[2:]
      #print "Added to question dict"
  queries = list()
  for qu in range(int(num_queries)):
    calc_queries(raw_input(), topics, questions)

main()
