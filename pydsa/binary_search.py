def binary_search(items_list, item,
                  recursive=False, first_ptr=-1, last_ptr=-1):
    """
    Searches the list 'items_list' for an item 'item'
    using binary search algorithm

    >>> from pydsa import binary_search
    >>> a = [1, 2, 7, 9, 10, 33, 56, 70, 99]
    >>> binary_search(a, 9)
    3
    >>> binary_search(a, 13)
    -1
    >>> binary_search(a, 13, True)
    -1
    >>> binary_search(a, 56, True)
    6
    >>> binary_search(a, 56, True, 0, 5)
    -1

    Binary Search
    Time Complexity:
        Average - O(logn)
        Best - O(1)
        Worst - O(1)

    Return value:   Index where element exists
                    -1 if element not found

    Input parameters: [items_list # List from which to search for item,
                        item # Item to search for,
                        recursive = True,
                        first_ptr = 0 # start of range inclusive,
                        last_ptr = len(items_list) # end of range inclusive]

    List provided should be sorted.
    """
    if first_ptr == last_ptr == -1:
        first_ptr = 0
        last_ptr = len(items_list) - 1

    if recursive:
        if last_ptr < first_ptr:
            return -1  # element not found.
        else:
            mid_ptr = first_ptr + ((last_ptr - first_ptr) // 2)
            if item == items_list[mid_ptr]:
                return mid_ptr
            elif item < items_list[mid_ptr]:
                return binary_search(items_list, item,
                                     True, first_ptr, mid_ptr - 1)
            else:  # item > items_list[mid_ptr]
                return binary_search(items_list, item,
                                     True, mid_ptr + 1, last_ptr)

    else:
        found = False
        index = -1  # element not found
        first_ptr = 0
        last_ptr = len(items_list) - 1
        while first_ptr <= last_ptr and not found:
            midpoint = (first_ptr + last_ptr) // 2
            if items_list[midpoint] == item:
                found = True
                index = items_list.index(item)
            else:
                if item < items_list[midpoint]:
                    last_ptr = midpoint - 1
                else:
                    first_ptr = midpoint + 1
        return index  # change to "return found" if only boolean required
