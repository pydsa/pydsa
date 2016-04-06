class Queue(object):
    def __init__(self):
        self.List = []

    def isEmpty(self):
        return not len(self.List)

    def enqueue(item):
        """
        Insert element in queue.
        """
        self.List.append(item)

    def dequeue(self):
        """
        Remove element from front of the Queue.
        """
        return self.List.popleft()

    def size(self):
        """
        Return size of Queue.
        """
        return len(self.List)
