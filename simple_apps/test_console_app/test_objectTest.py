import pytest

from test import Test as t


def t_with_1_q():
    return t('Когда ебали, что на жопе написали?', {'Молодец, я доволен': True})


def test_len_of_Test():
    assert len(t_with_1_q()) == 1


def test_str_return():
    assert str(t_with_1_q()) == 'Когда ебали, что на жопе написали?' + '\n' + '1. Молодец, я доволен'

def test_getitem():
    assert t_with_1_q()[0] == 'Молодец, я доволен'

def test_setitem():
    test_obj = t()
    test_obj.set_answer("Ответ", True)
    assert test_obj._test_answers['Ответ'] == True

def test_get_answer_value():
    assert t_with_1_q().get_answer_value(1)