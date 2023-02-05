from pali_leet import largest_palindrome

def test_palindrome():
    assert largest_palindrome('FFFFFF') == 'FFFFFF'
    assert largest_palindrome('POXYXYYXYXPO') == 'XYXYYXYX'
    assert largest_palindrome('POXYXYHYXYXPO') == 'XYXYHYXYX'