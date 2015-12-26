# Selection Sort
# Complexity: O(n^2)


def selection_sort(a):
    """Sorts an unsorted list a"""
    for i in range(len(a)):
        for j in range(i, len(a)):
            if(a[j] < a[i]):
                a[i], a[j] = a[j], a[i]
    return a
