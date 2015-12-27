# Quick Sort
# Complexity: Average Case: O(nlog(n))


def quick_sort(a, start=0, end=None):
    if end is None:
        end = len(a) - 1
    if(start < end):
        pIndex = _partition(a, start, end)
        quick_sort(a, start, pIndex-1)
        quick_sort(a, pIndex+1, end)
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
