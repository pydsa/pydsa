"""
Modular Multiplicative Inverse

Complexity: O(m)

Reference Used:
http://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/
"""


def mod_inverse(a, m):
    """
    Modular Multiplicative Inverse of two integers 'a' and 'm' is a positive
    integer 'x' less than m such that (ax) % m is 1.

    Finds modular inverse of 'a' modulo 'm' by checking for all integers from
    1 to 'm' and returns -1 if it doesn't exist.

    >>> from pydsa import mod_inverse
    >>> mod_inverse(3, 11)
    4
    >>> mod_inverse(2, 12)
    -1
    """
    a = a % m
    for x in range(1, m):
        if (a*x) % m == 1:
            return x

    return -1       # modular inverse of 'a' modulo 'm' doesn't exist.
