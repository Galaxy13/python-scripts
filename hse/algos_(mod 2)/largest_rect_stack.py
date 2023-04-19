def refresh_max(height, position, end, max_height):
    curr_max = (end - position[-1]) * height[-1]
    max_height = max(curr_max, max_height)
    height.pop()
    p = position.pop()
    return max_height, p


def max_rectang(hist: list) -> int:
    height = []
    position = []
    max_res = 0
    for i in range(len(hist)):
        if not height or hist[i] > height[-1]:
            height.append(hist[i])
            position.append(i)
        else:
            while height and height[-1] >= hist[i]:
                max_res, position_old = refresh_max(height, position, i, max_res)
            height.append(hist[i])
            position.append(position_old)
    while height:
        max_res, position_old = refresh_max(height, position, len(hist), max_res)

    return max_res

