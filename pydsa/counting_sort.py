# Counting Sort
# Complexity : O(n + (range of input))
# https://en.wikibooks.org/wiki/Algorithm_Implementation/Sorting/Counting_sort


def counting_sort(array, maxval):
    """
    Sorts the list 'array' using counting sort

    >>> from pydsa import counting_sort
    >>> a = [5, 6, 1, 9, 3]
    >>> counting_sort(a, 9)
    [1, 3, 5, 6, 9]

    """
    count = [0] * (maxval + 1)
    for a in array:
        count[a] += 1
    i = 0
    for a in range(maxval + 1):
        for c in range(count[a]):
            array[i] = a
            i += 1
    return array
