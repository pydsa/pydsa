from pydsa import bfs


def test_bfs():
    graph = {'A': set(['B', 'C']),
             'B': set(['A', 'D', 'E']),
             'C': set(['A', 'F']),
             'D': set(['B']),
             'E': set(['B', 'F']),
             'F': set(['C', 'E'])}
    assert bfs(graph, 'A') == set(['A', 'C', 'B', 'F', 'E', 'D'])
