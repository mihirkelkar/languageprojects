def max_prod(array):
  start_index = 0
  max_product = 0
  max_index = list()
  flag = 0
  for ii in range(len(array)):
    if array[ii] == 0 and ii >= start_index:
      flag = 1
      temp_product = max_prod_without_zeroes(array, start_index, ii)
      if max_product < temp_product:
        max_product = temp_product
      start_index = ii + 1
  if flag == 0:
    max_product = max_prod_without_zeroes(array, start_index, len(array) - 1)  
  return max_product

def max_prod_without_zeroes(array, start_index, end_index):
  first_negative_index = -1
  last_negative_index = - 1
  max_product = 0
  negative_count = 0
  for ii in range(start_index, end_index):
    if array[ii] < 0:
      negative_count += 1
      if first_negative_index == -1:
        first_negative_index = ii
      last_negative_index = ii
  if negative_count % 2 == 0:
    temp_product = max_product_without_negatives(array, start_index, end_index)    
  else:
    temp_product = max_product_with_negative(array, first_negative_index + 1, end_index)
    temp_product_two = max_product_with_negative(array, start_index , last_negative_index - 1)
    if temp_product < temp_product_two:
      temp_product = temp_product_two
  if temp_product > max_product:
    max_product = temp_product
  return max_product

def max_product_without_negative(array, start_index, end_index):
  product = 1
  for ii in range(start_index, end_index + 1):
    product *= array[ii]
  return prodcut

def max_product_with_negative(array, start_index, end_index):
  product = 1 
  for ii in range(start_index, end_index + 1):
    product *= array[ii]
  return product

print max_prod([-1, 25, 0 ,25, -1, -2])         
