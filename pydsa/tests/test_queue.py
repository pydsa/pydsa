from pydsa.queue import queue


def test_queue():
    q = queue()
    q.enqueue(5)
    q.enqueue(9)
    q.enqueue(12)
    q.enqueue(20)
    assert q.dequeue() == 5
    assert q.dequeue() == 9
    assert q.size() == 2
