#Start from the alst element in move forward towards the starting element. Keep the max element you find and 
#subtract every element you visit from it. Reutrn the max_answer
def largest_difference_pair(array):
  array_reverse = array[::-1]
  max_element = array[-1]
  max_d = 0
  for ii in array_reverse[1:]:
    if ii > max_element:
      max_element = ii
    else:
      if max_d < max_element - ii:
        max_d = max_element - ii
  return max_d

print largest_difference_pair([2, 4, 10, 2, 4, 8, 1])
    
