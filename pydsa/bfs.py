# Breadth First Search
# Complexity: O(V+E)

def bfs(graph,start):

	"""
	Traverses the graph 'graph' using Breadth First
	Search Algorithm. 

	>>> from pydsa import bfs
	>>> graph = {'A': set(['B', 'C']), 'B': set(['A', 'D', 'E']), 'C': set(['A', 'F']), 'D': set(['B']), 'E': set(['B', 'F']), 'F': set(['C', 'E'])}
	>>> bfs(graph,'A')
	['A', 'C', 'B', 'F', 'E', 'D']

	"""

	# mark every node unvisited
	visited , queue = {}, []
	for i in graph.keys():
		visited[i] = 0

	# final list of traversed nodes in the order
	final = []

	# mark given node visited and enqueue
	visited[start] = 1
	queue.append(start)

	while queue:

		# dequeue a node and append in the final list
		start = queue.pop(0)
		final.append(start)

		# check for all adjacent vertices of start vertex
		# if it is not visited, then mark and 
		# enqueue
		for i in graph[start]:
			if not visited[i]:
				visited[i] = 1
				queue.append(i)

	# return the final ordered list
	return final
