from pellet_best_strategy import solution

def test_should_return_best_strategy():
    assert solution('15') == 5
    assert solution('4') == 2
    assert solution('256') == 8