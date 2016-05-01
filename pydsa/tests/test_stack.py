from pydsa.stack import Stack


def test_stack():
    s = Stack()
    s.push(5)
    s.push(9)
    s.push(12)
    s.push(20)
    assert s.pop() == 20
    assert s.pop() == 12
    assert s.size() == 2
    assert s.pop() == 9
    assert s.pop() == 5
    assert s.is_empty() == True
