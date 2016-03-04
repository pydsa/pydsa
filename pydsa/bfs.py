# Breadth First Search
# Complexity: O(V+E)


def bfs(graph, start):
    """
    Traverses a graph using Breadth First Search Algorithm.
    It returns a set of nodes traversed.
    """
    visited, queue = set(), [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            # Add all the adjacent unvisited nodes to the queue
            queue.extend(graph[node] - visited)
    return visited
