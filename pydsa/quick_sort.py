# Quick Sort
# Complexity: Average Case: O(nlog(n))


def quick_sort(a, start=0, end=None):
    """
    Sorts the list 'a' using Quick sort algorithm

    >>> from pydsa import quick_sort
    >>> a = [3, 4, 2, 1, 12, 9]
    >>> quick_sort(a)
    [1, 2, 3, 4, 9, 12]

    """
    if end is None:
        end = len(a) - 1
    if (start < end):
        pIndex = _partition(a, start, end)
        quick_sort(a, start, pIndex - 1)
        quick_sort(a, pIndex + 1, end)
    return a


def _partition(a, start, end):
    pivot = a[end]
    j = start
    for i in range(start, end):
        if a[i] < pivot:
            a[i], a[j] = a[j], a[i]
            j += 1
    a[j], a[end] = a[end], a[j]
    return j
