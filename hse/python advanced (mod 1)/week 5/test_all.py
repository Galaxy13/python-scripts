from test_Complex import *

def test_check1():
    result, message = check1().split('\t')
    assert result == '1', message
    print(message)

def test_check2():
    result, message = check2().split('\t')
    assert result == '1', message
    print(message)

def test_check3():
    result, message = check3().split('\t')
    assert result == '1', message
    print(message)

def test_check4():
    result, message = check4().split('\t')
    assert result == '1', message
    print(message)
