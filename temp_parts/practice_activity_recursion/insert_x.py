def insert_x(my_string):
    if len(my_string) == 1:
        return my_string
    else:
        return my_string[0] + 'x' + insert_x(my_string[1:])


print(insert_x('catdog'))

if 3 != 2:
    print(2)
