from pydsa.linear_search import linear_search


def test_linear_search():
    List = [4, 17, 9, 12, 5, 16]
    item = 12
    assert linear_search(List, item) == 3
