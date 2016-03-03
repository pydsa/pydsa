"""

	Breadth-first search (BFS) is an algorithm 
	for traversing or searching tree or graph 
	data structures. It starts at the tree root 
	(or some arbitrary node of a graph, sometimes 
	referred to as a 'search key'[1]) and explores 
	the neighbor nodes first, before moving to 
	the next level neighbors.

	To find the Breadth First Search traversal
	order of a graph given in the form of 
	Adjacency Lists.
	Graph is traversed from the vertex k.

"""

def bfs(graph,k):
	# find number of nodes in the graph
	n = len(graph)

	# mark every node unvisited
	visited = [False for i in range(1,n+1)]
	queue = []

	# final list of traversed nodes in the order
	final = []

	# mark given node visited and enqueue
	visited[k] = True 
	queue.append(k)

	while queue:

		# dequeue a node and append in the final list
		k = queue[0]
		final.append(k)
		queue.pop(0)

		# check for all adjacent vertices of k
		# if it is not visited, then mark and 
		# enqueue
		for i in graph[k]:
			if not visited[i]:
				visited[i] = True
				queue.append(i)

	# return the final ordered list
	return final
