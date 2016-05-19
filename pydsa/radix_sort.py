# Radix Sort
# Reference used: http://www.geeksforgeeks.org/radix-sort/

BASE = 10


def radix_sort(a):
    """
    Sorts the list 'a' using Radix Sort algorithm.

    The idea is to do digit by digit sort starting from least significant
    digit to most significant digit.

    Complexity: Average Case: O(nlog(n)), where log is taken to the base for
    representing numbers. This implementation is for decimal system i.e. base
    is taken to be 10.

    >>> from pydsa import radix_sort
    >>> a = [708, 4567, 3, 45, 911, 123, 57, 37]
    >>> radix_sort(a)
    [3, 37, 45, 57, 123, 708, 911, 4567]

    """

    max_element = max(a)
    n = len(a)

    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is BASE^i
    # where i is current digit number
    exp = 1
    while max_element // exp > 0:
        _counting_sort(a, exp, n)
        exp *= BASE

    return a


def _counting_sort(a, exp, n):
    """Performs counting sort on list of length 'n' passed
    as 'a' according to the digit at the 'exp' place value.
    """

    output = [0] * (n)
    count = [0] * (BASE)

    # Store count of occurrences of digits in
    # 'exp' place value for each element of 'a'.
    for i in range(0, n):
        index = (a[i] // exp)
        count[(index) % BASE] += 1

    # Change count[i] so that count[i] now contains actual
    # position of this digit in output array.
    for i in range(1, BASE):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = (a[i] // exp)
        output[count[(index) % BASE] - 1] = a[i]
        count[(index) % BASE] -= 1

    for i in range(0, n):
        a[i] = output[i]
