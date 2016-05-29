# Heap Sort
# Complexity: O(nlog(n))


def heap_sort(list_item):
    """
    Heap Sort
    Time Complexity of Solution:
    Best - O(nlog(n))
    Average - O(nlog(n))
    Worst - O(nlog(n))

    Approach:
    Heap sort takes place in two steps. In first step, array is
    transformed into a heap.
    In second step, heap is continously reduced to a sorted array.

    """
    end = len(list_item)
    start = end // 2 - 1 # use // instead of /
    for i in range(start, -1, -1):
        heapify(list_item, end, i)
    for i in range(end-1, 0, -1):
        swap(list_item, i, 0)
        heapify(list_item, i, 0)

def heapify(list_item, end,i):
    left = 2 * i + 1        # Left Child
    right = 2 * (i + 1)     # Right Child
    max = i
    if left < end and list_item[i] < list_item[left]:
        max = left
    if right < end and list_item[max] < list_item[right]:
        max = right
    if max != i:
        swap(list_item, i, max)
        heapify(list_item, end, max)

def swap(list_item, i, j):
    list_item[i], list_item[j] = list_item[j], list_item[i]

