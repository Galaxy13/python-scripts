def remove_x(my_string):
    if len(my_string) == 0:
        return ''
    else:
        if my_string[0] != 'x':
            return my_string[0] + remove_x(my_string[1:])
        else:
            return remove_x(my_string[1:])

print(remove_x('catxxdogxx'))