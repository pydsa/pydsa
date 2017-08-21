# Bubble Sort
# Complexity: O(n^2)


def bubble_sort(a):
    """
    Sorts the list 'a' using Bubble sort algorithm

    >>> from pydsa import bubble_sort
    >>> a = [3, 4, 2, 1, 12, 9]
    >>> bubble_sort(a)
    [1, 2, 3, 4, 9, 12]

    """
    for k in range(len(a)):
        flag = 0
        for i in range(0, len(a) - k - 1):
            if (a[i] > a[i + 1]):
                a[i], a[i + 1] = a[i + 1], a[i]
                flag = 1
        if (flag == 0):
            break
    return a
