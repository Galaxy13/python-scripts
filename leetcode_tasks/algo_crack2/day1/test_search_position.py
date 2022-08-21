from search_insert_position import Solution as s

sol = s()

def test_search_position():
    assert sol.searchInsert([1,3,5,6], 5) == 2
    assert sol.searchInsert([1, 3, 5, 6], 2) == 1
    assert sol.searchInsert([1, 3, 5, 6], 7) == 4