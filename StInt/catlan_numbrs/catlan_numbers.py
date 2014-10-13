CATLAN_ARRAY = [1]

def catlan_numbers(number):
  for ii in range(0, number - 1):
    result += CATLAN_ARRAY[ii] * CATLAN_ARRAY[number - 1 - ii]


#THis is a simple function that you can now put to use anywhewre you want
