from pydsa.mod_inverse import mod_inverse


def test_mod_inverse():
    assert mod_inverse(3, 13) == 9
    assert mod_inverse(30, 120000) == -1
