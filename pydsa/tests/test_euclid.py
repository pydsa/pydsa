from pydsa.euclid import extended_euclid
from pydsa.euclid import gcd

def test_gcd():
    assert gcd(4, 10) == 2
    assert gcd(89, 23) == 1
    assert gcd(1024, 512) == 512
    assert gcd(116127, 15433) == 253

def test_extended_euclid():
    assert extended_euclid(4, 10) == (2, -2, 1)
    assert extended_euclid(89, 23) == (1, -8, 31)
    assert extended_euclid(1024, 512) == (512, 0, 1)
    assert extended_euclid(116127, 15433) == (253, 21, -158)
