def insertion_sort(a):
    """
    Sorts the list 'a' using insertion sort algorithm

    >>> from pydsa import insertion_sort
    >>> a = [3, 4, 2, 1, 12, 9]
    >>> insertion_sort(a)
    [1, 2, 3, 4, 9, 12]

    """
    for i in range(1, len(a)):
        element = a[i]
        j = i
        while j > 0 and a[j - 1] > element:
            a[j] = a[j - 1]
            j = j - 1
        a[j] = element
    return a
