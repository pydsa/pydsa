# Gnome Sort
# Complexity : O(n^2)
# https://en.wikibooks.org/wiki/Algorithm_Implementation/Sorting/Gnome_sort


def gnome_sort(a):
    """
    Sorts the list 'a' using gnome sort
    >>> from pydsa import gnome_sort
    >>> a = [5, 6, 1, 9, 3]
    >>> gnome_sort(a)
    [1, 3, 5, 6, 9]
    """
    i = 0
    while i < len(a):
        if i != 0 and a[i] < a[i-1]:
            a[i], a[i-1] = a[i-1], a[i]
            i -= 1
        else:
            i += 1
    return a
