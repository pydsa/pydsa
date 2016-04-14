class queue(object):
    """
    A queue is a container of objects (a linear collection)
    that are inserted and removed according to the
    first-in first-out (FIFO) principle.

    >>> from pydsa import queue
    >>> q = queue()
    >>> q.enqueue(5)
    >>> q.enqueue(8)
    >>> q.enqueue(19)
    >>> q.dequeue()
    5
    """
    def __init__(self):
        self.List = []

    def isEmpty(self):
        return self.List == []

    def enqueue(self, item):
        """
        Insert element in queue.
        """
        self.List.append(item)

    def dequeue(self):
        """
        Remove element from front of the Queue.
        """
        return self.List.pop(0)

    def size(self):
        """
        Return size of Queue.
        """
        return len(self.List)
