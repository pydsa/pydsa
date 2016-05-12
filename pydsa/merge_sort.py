# Merge Sort
# Complexity: O(nlog(n))


def _merge(L, R):
    m, i, j = [], 0, 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            m.append(L[i])
            i += 1
        else:
            m.append(R[j])
            j += 1
    if i == len(L):
        m.extend(R[j:])
    else:
        m.extend(L[i:])
    return m


def merge_sort(a):
    """
    Sorts the list 'a' using Merge sort algorithm

    >>> from pydsa import merge_sort
    >>> a = [3, 4, 2, 1, 12, 9]
    >>> merge_sort(a)
    [1, 2, 3, 4, 9, 12]

    """
    l = len(a)
    if l >= 2:
        L = a[0:l // 2]
        R = a[l // 2:]
        a = _merge(merge_sort(L), merge_sort(R))
    return a
