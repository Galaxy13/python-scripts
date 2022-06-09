from linear_progression_complex import solution

def test_should_return_right_final_value():
    assert solution(1, 1) == '1'
    assert solution(4, 1) == '10'
    assert solution(1, 4) == '7'
    assert solution(2, 2) == '5'
    assert solution(3, 2) == '9'

