class Stack(object):
    """
    A stack is a container of objects that are inserted
    and removed according to the last-in first-out (LIFO) principle.

    >>> from pydsa import stack
    >>> s = Stack()
    >>> s.push(9)
    >>> s.push(90)
    >>> s.push(19)
    >>> s.push(1)
    >>> s.size()
    4
    >>> s.pop()
    1
    >>> s.pop()
    19
    """
    def __init__(self):
        self.List = []

    def is_empty(self):
        return self.List == []

    def push(self, item):
        """
        Insert element in stack.
        """
        self.List.append(item)

    def pop(self):
        """
        Remove element which inserted last in stack.
        """
        return self.List.pop()

    def size(self):
        """
        Return size of stack.
        """
        return len(self.List)
