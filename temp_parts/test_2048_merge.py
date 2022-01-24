"""
Merge function for 2048 game.
"""


def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    new_line = []
    # this loop creates list, without zeros
    for tile in line:
        if tile != 0:
            new_line.append(tile)
    # this loop sum required tiles
    for index, tile in enumerate(new_line):
        if index + 1 < len(new_line):
            if tile == new_line[index + 1]:
                new_line[index] += tile
                new_line.pop(index + 1)

    if len(new_line) < len(line):
        for dummy_variable in range(len(line) - len(new_line)):
            new_line.append(0)
    return new_line
