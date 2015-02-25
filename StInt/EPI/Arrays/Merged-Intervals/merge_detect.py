class Event(object):
  def __init__(self, start, end):
    self.start = start
    self.end = end

  def print_times(self):
    print self.start, 
    print self.end

def find_merge_intervals(list_of_intervals):
  sorted_list = sorted(list_of_intervals, key = lambda x : x.start)
  for ii in range(1, len(sorted_list)):
    if sorted_list[ii - 1].end >= sorted_list[ii].start:
      sorted_list[ii].start = sorted_list[ii - 1].start
      if sorted_list[ii - 1].end > sorted_list[ii].end:
        sorted_list[ii].end = sorted_list[ii - 1].end
      sorted_list[ii - 1] = None

  return [ii for ii in sorted_list if ii != None]

def main():
  a = Event(1, 3)
  b = Event(2, 6)
  c = Event(8, 10)
  d = Event(15, 18)
  temp_list = find_merge_intervals([a, b, c, d]) 
  for ii in temp_list:
    ii.print_times()   
  
if __name__ == "__main__":
  main()
