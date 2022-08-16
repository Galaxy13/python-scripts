from Binary_search_704 import Solution as Sol

sol = Sol()

def test_binary_search_alg():
    assert sol.search([1, 4, 7, 9], 4) == 1
    assert sol.search([1], 2) == -1
    assert sol.search([2], 2) == 0
    assert sol.search([0, 1, 2, 4, 6, 9], 9) == 5
