import sys
import re
class Circuit(object):
  def __init__(self, line):
    self.score_list = [int(ii) for ii in re.findall(r"\w:(\d+)", line)]
    self.members = list()
    self.circuit_scores_for_members = list()

class Juggler(object):
  def __init__(self, line):
    self.juggler_number = int(re.findall(r"J(\d+)", line)[0])
    self.juggler_scores = [int(ii) for ii in re.findall("\w:(\d+)", line)]
    self.prefs = [int(ii) for ii in re.findall(r"C(\d+)", line)]
    self.pref_scores = list()
    for ii in self.prefs:
      self.pref_scores.append(calc_pref_scores(ii, self.juggler_scores))
    #print self.pref_scores
    #print "================="
    self.circuit_to_score_map = dict(zip(self.prefs, self.pref_scores))
    #print self.circuit_to_score_map
      
def calc_pref_scores(ii, juggle_scores):
  global circuits
  circuit_scores = circuits[ii].score_list
  score =  sum([circuit_scores[ii] * juggle_scores[ii] for ii in range(3)])
  return score

def make_outputs():
  global circuits
  write = open('output', 'w')
  output_list = list()
  for index, ii in enumerate(circuits):
    string = "C%s"%index
    for ind, elem in enumerate(ii.members):
      temp = elem.circuit_to_score_map.items()
      string+= " J%s"%elem.juggler_number
      for cc in range(len(temp)):
        string += " C%s:%s"%(temp[cc][0], temp[cc][1])
      if ind != len(ii.members) - 1:
        string += ","
    output_list.append(string)
  write.write("\n".join(output_list))
  write.close()


  
circuits = []
jugglers = []
fp = open(sys.argv[1], 'r').readlines()
for line in fp:
  if line == "\n":
    pass
  elif line[0] == "C":
    circuits.append(Circuit(line.strip()))
  elif line[0] == "J":
    jugglers.append(Juggler(line.strip()))

member_per_team = len(jugglers) / len(circuits)    
while jugglers:
  #Iterate through jugglers, retrieve a juggler
  juggler = jugglers.pop()
  #Get the jugglers prefernces
  preference = juggler.prefs
  #print juggler.prefs
  #Iterate through preferences.
  for ii in preference:
    #print "Entered the preference loop"
    #If you can fit into a prefernce , fit there
    #print len(circuits[ii].members), member_per_team
    if len(circuits[ii].members) < member_per_team:
      #print "Added juggler %s to circuit %s" %(juggler.juggler_number, ii)      
      circuits[ii].members.append(juggler)
      circuits[ii].circuit_scores_for_members.append(juggler.circuit_to_score_map[ii])
      break
    else:
      #If you cant fit, knock someone out and fit
      small = 0
      #print circuits[ii].circuit_scores_for_members
      for scores in circuits[ii].circuit_scores_for_members:
        if scores < juggler.circuit_to_score_map[ii]:
          small = 1
      if small == 1:
        index = circuits[ii].circuit_scores_for_members.index\
              (min(circuits[ii].circuit_scores_for_members))
        jugglers.append(circuits[ii].members.pop(index))
        circuits[ii].circuit_scores_for_members.pop(index)
        circuits[ii].members.append(juggler)
        break

make_outputs()
#print sum([ii.juggler_number for ii in circuits[1970].members])
