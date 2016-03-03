# Breadth First Search
# Complexity: O(V+E)

def bfs(graph,start):

	"""
	Traverses the graph 'graph' using Breadth First
	Search Algorithm. 

	>>> from pydsa import bfs
	>>> a = [[1,2],[2],[0,3],[3]]
	>>> bfs(a,2)
	[2,0,3,1]

	"""

	# find number of nodes in the graph
	n = len(graph)

	# mark every node unvisited
	visited = [False for i in range(1,n+1)]
	queue = []

	# final list of traversed nodes in the order
	final = []

	# mark given node visited and enqueue
	visited[start] = True 
	queue.append(start)

	while queue:

		# dequeue a node and append in the final list
		start = queue[0]
		final.append(start)
		queue.pop(0)

		# check for all adjacent vertices of start vertex
		# if it is not visited, then mark and 
		# enqueue
		for i in graph[start]:
			if not visited[i]:
				visited[i] = True
				queue.append(i)

	# return the final ordered list
	return final
