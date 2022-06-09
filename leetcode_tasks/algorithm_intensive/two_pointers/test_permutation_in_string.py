from Permutation_in_String import Solution


def test_should_return_True():
    solution = Solution()

    assert solution.checkInclusion('ab', 'ab')
    assert solution.checkInclusion('ab', 'abc')
    assert solution.checkInclusion('abc', 'rtyabcort')
    assert solution.checkInclusion('r', 'tghoymcxwr')
    assert solution.checkInclusion('ab', 'eidbaooo')


def test_should_return_False():
    solution = Solution()

    assert not solution.checkInclusion('ab', 'cd')
    assert not solution.checkInclusion('rt', 'rdt')
    assert not solution.checkInclusion('a', 'b')
    assert not solution.checkInclusion('ab', 'eidboaoo')
    assert not solution.checkInclusion('aba', 'abba')
    assert not solution.checkInclusion('ab', 'a')
    assert not solution.checkInclusion("dinitrophenylhydrazine", "acetylphenylhydrazine")

def test_should_return_all_permuataions():
    solution = Solution()

    assert solution.permutations('ab') == ['ab', 'ba']
    assert solution.permutations('abc') == ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']