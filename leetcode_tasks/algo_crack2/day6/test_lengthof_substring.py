from longest_substring_repeating_3 import Solution as s

sol = s().lengthOfLongestSubstring

def test_sliding_substring():
    assert sol("abcabcbb") == 3
    assert sol("bbbbb") == 1
    assert sol('pppwkebbbbbb') == 5
    assert sol('') == 0
    assert sol('avcvvvvvvvvvvbnm') == 4
    assert sol(' ') == 1
    assert sol('pa') == 2