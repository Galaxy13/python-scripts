from number_of_salutes import solution

def test_should_count_salutes():
    assert solution('--><') == 2
    assert solution('<<<<<<>') == 0
    assert solution('>----<') == 2
    assert solution('<<>><') == 4
    assert solution('<>') == 0
    assert solution('->>>>><') == 10