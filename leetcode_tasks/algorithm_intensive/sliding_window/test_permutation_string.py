from Permutation_ins_string import Solution

# def test_should_return_freq_dict_of_s1_depr():
#     func = Solution().checkInclusion
#
#     assert func('abc', '') == {'a': 1, 'b': 1, 'c':1}
#     assert func('aaa', '') == {'a': 3}
#     assert func('', '') == {}
#     assert func('aabbcd', '') == {'a': 2, 'b':2, 'c':1, 'd':1}

def test_should_return_perm_bool():
    func = Solution().checkInclusion

    assert func('ab', 'eidbaooo') is True
    assert func()