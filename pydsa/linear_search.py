def linear_search(List, item):
    """
    Find the element in list using linear search
    >>> from pydsa import linear_search
    >>> List = [3, 4, 6, 8, 12, 15, 26]
    >>> item = 6
    >>> linear_search(List, item)
    2
    """
    index = len(List)
    for i in range(0, index):
        if List[i] == item:
            return i
    return -1
