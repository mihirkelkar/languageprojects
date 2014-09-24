import unittest

"""
  ========================================================
  Calculates Cluster of Lakes from a given input of co-ords
  Time complexity : O(n) --> Filter elements
                    O(n) --> Build hash z_index
                    O(8n) --> Construct graph
                    BFS invloved -> 0( len(path) * n + constant) 
                    because it was slightly modified
  Asymptototic : O(kN)  
  ========================================================
"""
def find_lakes(pts, threshold):
  global border_points
  #Points is assumed to a be a list of tuples. eg[(1,2,3), (1,3,5)]
  #Finding points below threshold
  
  below_w_level = [ii for ii in pts if ii[2] < threshold] 

  #Building a map of z-indices to reconstruct 3d co-ords later
  #This has to be done to take care of situations where co-ords like
  #(1, 2, 1) and (1, 2, 7) are given simulatneously. 
  z_index_map = {}
  for ii in below_w_level:
    try:
      z_index_map[(ii[0], ii[1])].append(ii[2])
    except:
      z_index_map[(ii[0], ii[1])] = [ii[2]]

  #Retreving 2d cords only
  below_w_level = z_index_map.keys()

  #Creating an adjacency hash in O(8n) time
  graph = dict(zip(below_w_level,[ [] for ii in range(len(below_w_level))]))
  for tuple in graph.keys():
    for mv in [(1,0), (1,-1), (1,1), (0,1),(0,-1),(-1,1),(-1,-1),(-1,0)]:
      try:
        temp = graph[(tuple[0] + mv[0], tuple[1] + mv[1])]
        graph[tuple].append((tuple[0] + mv[0], tuple[1] + mv[1]))
      except:
        pass
  #Doing a breadth first search and looking for separate connected compenents 
  #in the graph
  cluster_groups = breadth_first_search(graph)
  #Reconstructing 3d indices
  cluster_groups = build_3d_cluster(cluster_groups, z_index_map)
  #Returning indices of lakes in the unit.
  return cluster_groups



def build_3d_cluster(cluster_groups, z_index_map):
  for index, cluster in enumerate(cluster_groups):
    temp_cluster = []
    for tuple in cluster:
      for ii in z_index_map[tuple]:
        temp_cluster.append((tuple[0], tuple[1], ii))
    cluster_groups[index] = temp_cluster
  return cluster_groups


  
def breadth_first_search(graph):
  #Just a plain BFS Modified for my use
  visited_nodes = []
  cluster_groups = []
  for ii in graph.keys():
    if ii not in visited_nodes:
      temp_cluster = []
      start_seed = [ii]
      while start_seed:
        temp = start_seed.pop(0)
        if temp not in visited_nodes:
          visited_nodes.append(temp)
          temp_cluster.append(temp)
          start_seed += [el for el in graph[temp] if el not in visited_nodes ]
      cluster_groups.append(temp_cluster) 
  return cluster_groups



def find_polygon_area(vertices):
  #Unroll the area like a shoelace and keep adding to area
  area = 0.0
  for ii in range(4):
    jj = (ii + 1) % 4
    area += vertices[ii][0] * vertices[jj][1]
    area -= vertices[jj][0] * vertices[ii][1]
  return abs(area) / 2


"""
================================================
Find extreme vertices and then calculate an area.
Time complexity: 0(nLogn) for all 4 Timsorts (Internal Python sort)
                 find_polygon always iterates over 4 instances:
=============================================== 

"""
def find_area(cluster):
  #Estimate 4 co-ordinates that can demarkate extremeities. 
  #Then use the polygon area to calculate approximate area. 
  x_cords = [xx[0] for xx in cluster].sort()
  y_cords = [yy[1] for yy in cluster].sort()
  if xx[0] == xx[-1] or yy[0] == yy[-1]:
    return len(cluster)
  else:
    x = sorted(cluster, key = lambda ii: (ii[0], ii[1]))
    y = sorted(cluster, key = lambda ii: (ii[1], ii[0]))
    vx_1, vx_2 = x[0], [ii for ii in x if ii[0] == x[-1][0]][0]
    vy_1, vy_2 = y[-1],[ii for ii in y if ii[1] == y[-1][1]][0]
  return find_polygon_area([vx_1, vx_2, vy_1, vy_2])  


"""
==========================================
Find volume of the polygons generated. 
Time complexity == Time complexity of above function
==========================================
"""
def find_volume(cluster):
  #Calculate surface area and multiply it by average depth.
  z_indices = [ii[2] for ii in cluster]
  z_average = float(sum(z_indices)) / float(len(z_indices))
  water_level = min(z_indices) + 1
  return find_area(cluster) * (water_level - z_average) 


def trace_path(parent, start, end):
  #Trace the shortest path from start to end
  path = [end]
  while path[-1] != start:
    path.append(parent[path[-1]])
  return path[::-1]


"""
 Plain simple BFS. 0(e) + graph construction.
"""
def shortest_path_A_B(points, start, target, gradient):
  #A Breadth Forst Search is guaranteed to find thr shortest path between 
  #a source and a destination.
  graph = construct_graph(points) 
  visited = []   
  parent = {}
  que = []
  que.append(start)
  while que:
    node = que.pop(0)
    if node == target:
      return trace_path(parent, start, target) 
    for adj in graph.get(node):
      if abs(node[2] - adj[2]) < gradient and adj not in visited:
        que.append(adj)
        parent[adj] = node
        visited.append(adj)


"""
  Linear time for constructing a 2d graph.
  O(n ^ i) i < 2 for constructing a 3d adjaceny graph
"""  
def construct_graph(points):
  #Accept points, make a 2d adjanceny graph. 
  #Convert it into a 3d adjacency graph and return to the shortest path function. Thats it. 
  z_index_map = {}
  for ii in points:
    try:
      z_index_map[(ii[0], ii[1])].append(ii[2])
    except:
      z_index_map[(ii[0], ii[1])] = [ii[2]]
  points = z_index_map.keys()
  graph = dict(zip(points,[ [] for ii in range(len(points))]))

  for tuple in graph.keys():
    for mv in [(1,0), (1,-1), (1,1), (0,1),(0,-1),(-1,1),(-1,-1),(-1,0)]:
      try:
        temp = graph[(tuple[0] + mv[0], tuple[1] + mv[1])]
        graph[tuple].append((tuple[0] + mv[0], tuple[1] + mv[1]))
      except:
        pass
  #Constructing a 3d adjacency matrix
  t_d_graph = {}
  for ii in graph.items():
    keys = [(ii[0][0], ii[0][1], z_index) for z_index in z_index_map[ii[0]]]
    values = []
    for val in ii[1]:
      values += [(val[0], val[1], z_index_val) for z_index_val in z_index_map[val]]
    for num in keys:
      t_d_graph[num] = values
  return t_d_graph  



points = [(0, 0, 0), (0, 1, 0), (0, 2, 0), (1, 1, 2), (1, 1, 3), (2, 1, 0), (2, 2, 0)]
lakes = find_lakes(points, 2)

class LakeTest(unittest.TestCase): 
  global points
  global lakes
  def test_lakes(self):
    #self.points = [(0, 0, 0), (0, 1, 0), (0, 2, 0), (1, 1, 2), (1, 1, 3), (2, 1, 0), (2, 2, 0)]
    expected_ans = [[(0, 1, 0), (0, 2, 0), (0, 0, 0)],[(2, 1, 0), (2, 2, 0)]]
    for index, ii in enumerate(lakes):
      print "Lake no %s is as follows:" %(index)
      print ii
      print "-" * 60
    self.assertEqual(expected_ans, lakes)
  
  def test_area(self):
    lake_areas = [find_area(lake) for lake in lakes]
    lake_index = lake_areas.index(max(lake_areas))
    lake_volumes = [find_volume(lake) for lake in lakes]
    lake_vol_in = lake_volumes.index(max(lake_volumes))
    print "Lake %s has a max area, which is %s" %(lake_index, lake_areas[lake_index])
    print " = " * 60
    print "lake %s has a max volume, which is %s" %(lake_vol_in, lake_volumes[lake_vol_in])
    self.assertEqual(3.0, lake_areas[lake_index])
    print "Max area verified"
    self.assertEqual(3.0, lake_volumes[lake_vol_in])
    print "max volume verified"
   
  def test_short_path(self):
    answer = None
    self.assertEqual(shortest_path_A_B(points, (0,0,0), (2,2,0), 2), None, "Shortest Path confirmed")
    print "No shortest path should exist. Thats verified"
    points.append((1,1,1))
    answer = [(0,0,0), (1,1,1), (2,2,0)]
    self.assertEqual(shortest_path_A_B(points, (0,0,0), (2,2,0), 2), answer)
    print "Shortest Path exists.Its correct and verified"
    print answer
if __name__ == "__main__":
  unittest.main()
