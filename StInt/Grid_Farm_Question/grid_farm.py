import collections

cluster_points = list()
def clusters_in_grid_farm(grid_farm):
  cluster_count = 0
  for ii in range(len(grid_farm)):
    for jj in range(len(grid_farm[0])):
      if (ii, jj) not in cluster_points:
        cluster_new = find_cluster(ii, jj, grid_farm)
        if cluster_new:
          cluster_count += 1
  return cluster_count

def find_cluster(ii, jj, grid_farm):
  global cluster_points
  cluster_list = list()
  if grid_farm[ii][jj] == 'Y' and (ii, jj) not in cluster_points:
    cluster_list.append((ii, jj))
    cluster_points.append((ii, jj))
    if ii < len(grid_farm) - 1:
    #move down the grid to check
      cluster_list += find_cluster(ii + 1, jj, grid_farm)
    if ii > 0:
      cluster_list += find_cluster(ii - 1, jj, grid_farm)
    if jj > 0:
      cluster_list += find_cluster(ii, jj - 1, grid_farm)
    if jj < len(grid_farm[0]) - 1:
      cluster_list += find_cluster(ii, jj + 1, grid_farm) 
  return cluster_list

def factorial(number):
  if number <= 0:
    return 1
  else:
    factorial = 1
    while number >= 1:
      factorial *= number
      number -= 1
  return factorial
def even_cow_combinations_in_grid():
  #This is basically just n P r ing through all even numbers less than or equal to n and summing them up. 
  n = clusters_in_grid_farm([['Y', 'N', 'N', 'Y'], ['N', 'Y', 'N', 'Y'], ['N', 'Y', 'N', 'N']])
  sum = 0
  for rr in range(0, n + 1, 2):
    sum += factorial(n) / (factorial(n - rr) * factorial(rr))
  return sum

print even_cow_combinations_in_grid()

    
      
   
