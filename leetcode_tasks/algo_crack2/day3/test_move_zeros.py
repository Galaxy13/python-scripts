import pytest

from move_zeros_283 import Solution as s

def testcase1():
    return s().moveZeroes

def test_move_zeros():
    # assert testcase1()([0,1,0,3,12])
    assert testcase1()([0,0,1])