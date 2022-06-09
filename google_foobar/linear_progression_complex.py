def solution(x, y):
    return str(int(((2 * x + y - 2) / 2) * (y - 1) + ((x + x ** 2) / 2)))


def solution_depricated(x, y):
    start_x = int((x + x ** 2) / 2)
    if y > 1:
        final_y = int(((2 * x + y - 2) / 2) * (y - 1) + start_x)
    else:
        final_y = start_x
    return str(final_y)
