def recursion_sort(array: list) -> list:
    if len(array) <= 1:
        return array
    return recursion_sort([x for x in array[1:] if x <= array[0]]) + [array[0]] \
           + recursion_sort([x for x in array[1:] if x > array[0]])


print(recursion_sort([3, 6, 2, 8, 4, 1, 0]))
