def list_reverse(my_list):
    if len(my_list) == 1 or len(my_list) == 0:
        return my_list
    else:
        return [my_list[-1]] + list_reverse(my_list[1:-1]) + [my_list[0]]

print(list_reverse([2,3,1,4,5,1]))