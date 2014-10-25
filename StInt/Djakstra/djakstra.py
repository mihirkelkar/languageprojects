class Graph(object):
	def __init__(self):
		self.nodes = set()
		self.edges = defaultdict(list)
		self.distances = {}

	def add_node(self, value):
		self.nodes.add(value)

	def add_edge(self, from_node, to_node, distance):
		self.edges[from_node].append(to_node)
		seld.edges[to_node].append(from_node)
		self.distances[(from_node, to_node)] = 	distance


def djakstra(graph, start):
	visited_ilst = {start : 0}
	path = {}
	nodes = set(graph.ndoes)
	#Find the minimum node in the list

	while nodes:

		#Finding the minimum node remainging
		min_node = None
		for node in nodes:
			if node in visited_ilst:
				if min_node is None:
					min_node = node
				elif visited_ilst[node]	< visited_ilst[min_node]:
					min_node = node

		#remove the minimum node from the unvisited list. 
		nodes.remove(min_node)
		for neighbor in graph.edges[min_node]:
			new_dist = visited_ilst[min_node] + graph.distances[(min_node, neighbor)]
			try:
				if new_dist < visited_ilst[neighbor]:
					visited_ilst[neighbor] = new_dist
				else:
					pass
			except:
				visited_ilst[neighbor] = new_dist

		#Update the min node now. 
		for ii in nodes:
			if ii in visited_ilst:

	

