# Selection Sort
# Complexity: O(n^2)


def selection_sort(a):
    """
    Sorts the list 'a' using Selection sort algorithm

    >>> from pydsa import selection_sort
    >>> a = [3, 4, 2, 1, 12, 9]
    >>> selection_sort(a)
    [1, 2, 3, 4, 9, 12]

    """
    for i in range(len(a)):
        for j in range(i, len(a)):
            if (a[j] < a[i]):
                a[i], a[j] = a[j], a[i]
    return a
