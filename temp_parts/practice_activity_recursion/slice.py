def slice(my_list, first, last):
    if len(my_list) == 0: return []
    if first >= last - 1:
        return [my_list[first]]
    else:
        return [my_list[first]] + slice(my_list, first + 1, last)

print(slice([1, 2, 3], 1, 2))


def test_slice():
    """
    Some test cases for slice
    """
    print("Computed:", slice([], 0, 0), "Expected: []")
    print("Computed:", slice([1], 0, 0), "Expected: []")
    print("Computed:", slice([1], 0, 1), "Expected: [1]")
    print("Computed:", slice([1, 2, 3], 0, 3), "Expected: [1, 2, 3]")
    print("Computed:", slice([1, 2, 3], 1, 2), "Expected: [2]")


test_slice()