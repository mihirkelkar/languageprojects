#The greedy approach to the two partition problem. 
def find_partition(list_s):
  list_one = []
  list_two = []
  list_s = sorted(list_s, reversed = True)
  for ii in list_s:
    if sum(list_a) <= sum(list_b):
      list_a.append(ii)
    else:
      list_b.append(ii)

