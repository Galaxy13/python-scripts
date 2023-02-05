import math


def can_escape(maze, i=0, j=0):
    n = len(maze)
    m = len(maze[0])
    if i == n - 1 and j == m - 1:
        return True
    maze[i][j] = 1
    result = False
    for a, b in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
        if 0 <= a < n and 0 <= b < m and maze[a][b] == 0:
            result = result or can_escape(maze, a, b)
    maze[i][j] = 0
    return result


def fastest_escape_length(maze):
    def recursive_escape(maze_inner, row, col):
        if row == len(maze_inner) - 1 and col == len(maze_inner[0]) - 1:
            return True
        result = False
        maze_inner[row][col] = 1
        for a, b in [(row - 1, col), (row, col - 1), (row + 1, col), (row, col + 1)]:
            if 0 <= a < len(maze_inner) and 0 <= b < len(maze_inner[0]) and maze_inner[a][b] == 0:
                result = min(result, (recursive_escape(maze_inner, a, b)))
        maze_inner[row][col] = 0
        return result + 1

    return recursive_escape(maze, 0, 0)


def fastest_escapes(maze):
    routes = []

    def recursive_escapes(maze_inner, route=[], row=0, col=0):
        route.append((row, col))
        if row == len(maze_inner) - 1 and col == len(maze_inner[0]) - 1:
            if not len(routes) or len(routes[0]) == len(route):
                routes.append(route.copy())
            elif len(route) < len(routes[0]):
                routes.clear()
                routes.append(route.copy())
        maze_inner[row][col] = 1
        for a, b in [(row - 1, col), (row, col - 1), (row + 1, col), (row, col + 1)]:
            if 0 <= a < len(maze_inner) and 0 <= b < len(maze_inner[0]) and maze_inner[a][b] == 0:
                recursive_escapes(maze_inner, route, a, b)
        maze_inner[row][col] = 0
        route.pop()

    recursive_escapes(maze)
    return sorted(routes)


def weighted_escape_length(maze, w):
    def recursive_escape(maze_inner, row, col):
        if row == len(maze_inner) - 1 and col == len(maze_inner[0]) - 1:
            return 1
        result = math.inf
        for a, b in [(row - 1, col), (row, col - 1), (row + 1, col), (row, col + 1)]:
            if 0 <= a < len(maze_inner) and 0 <= b < len(maze_inner[0]) and maze_inner[row][col] != 2:
                prev_value = maze_inner[row][col]
                maze_inner[row][col] = 2
                result = min(result, (recursive_escape(maze_inner, a, b)))
                maze_inner[row][col] = prev_value
        return result + w if maze_inner[row][col] else result + 1

    return recursive_escape(maze, 0, 0)


def weighted_escapes(maze, w):
    routes = []
    min_real_length = [math.inf]

    def recursive_escapes(maze_inner, route=[], row=0, col=0, real_lehgth=0):
        route.append((row, col))
        if row == len(maze_inner) - 1 and col == len(maze_inner[0]) - 1:
            if not len(routes) or min_real_length[0] == real_lehgth:
                routes.append(route.copy())
            elif real_lehgth < min_real_length[0]:
                routes.clear()
                routes.append(route.copy())
                min_real_length[0] = real_lehgth
            route.pop()
            return
        prev_value = maze_inner[row][col]
        maze_inner[row][col] = 2
        for a, b in [(row - 1, col), (row, col - 1), (row + 1, col), (row, col + 1)]:
            if 0 <= a < len(maze_inner) and 0 <= b < len(maze_inner[0]) and maze_inner[a][b] != 2:
                if not prev_value:
                    recursive_escapes(maze_inner, route, a, b, real_lehgth + 1)
                else:
                    recursive_escapes(maze_inner, route, a, b, real_lehgth + w)
        maze_inner[row][col] = prev_value
        route.pop()

    recursive_escapes(maze)
    return sorted(routes)

# can_escape()

maze = [

      [0, 0, 1, 0],

      [0, 0, 0 , 0],

      [0, 1, 0 , 0],

     [0, 1, 0 , 0]

    ]
print(weighted_escapes(maze, 1))
