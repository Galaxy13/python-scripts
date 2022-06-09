import remove_n_in_list

def test_should_remove_elem_if_quanitiy_is_n():
    assert remove_n_in_list.solution([1, 2, 4, 6, 4, 9], 1) == [1, 2, 6, 9]
    assert remove_n_in_list.solution([1, 2, 2, 3, 3, 3, 4, 5, 5], 1) == [1, 4]
    assert remove_n_in_list.solution([1,2,3], 0) == []