#I am going to use a XOR function here. Every number that appears in even terms will be zero, the remaning term (which is the only term in this case) will remain

def calculate_odd_term(array):
  num = array[0]
  for ii in range(1, len(array)):
    num = num ^ array[ii]
  return num

print calculate_odd_term([1, 1, 2, 2, 3])  
