# Here we have assumed that the capacity of each glass is only 1 liter. 

def find_water(row_number, column_number, water):
  //Ith row can only contain i glasses, so if your galss numberis greater than
  //the row number, then the input is wrong. 
  if column_number > row_number:
    print "No such glass can exist. Exiting"
    sys.exit(1)
  else:
    number_of_glasses = row_number * (row_number + 1) / 2
    glass_list = [0 for ii in range(number_of_glasses)]
  #iterate through all the given rows till you reach the row you need to target.
    row = 0
    while( row < row_number and water != 0):
      column = 0
      index = 0
      while(column < column_number):
        #Get the water from the current glass
        water_in_glass = glass_list[index]
        #Now adjust the amount to be max of either the capacity or the water 
        #water in the glass. 
        glass_list[index] = max(1, water_in_glass)
        water = water  - 1 if water > 1 else 0
        glass[index + row] += water / 2
        glass[index + row + 1] += water / 2  
