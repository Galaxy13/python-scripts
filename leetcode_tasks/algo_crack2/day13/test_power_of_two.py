from power_of_two_bit_231 import *

sol = Solution().isPowerOfTwo

def test_is_power_if_two():
    assert not sol(0)
    assert sol(1)
    assert not sol(-2)
    assert not sol(-3)
    assert sol(2)
    assert sol(1024)
    assert not sol(1025)