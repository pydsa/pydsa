from pydsa import bfs

def test_bfs():
	graph = [[1,2],[2],[0,3],[3]]
	bfs_order = bfs(graph,2)
	assert bfs_order == [2,0,3,1]