import random

GRID_TYPES = {'wall': 1,
              'path': 2,
              'enemy': 3}

class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[None for _ in range(height)] for _ in range(width)]

    def draw_grid(self):
        for x in range(self.width):
            for y in range(self.height):
                print('%%-%ds' % 2 % ".", end='')
            print()

    def is_allowed(self, coordinates):

    def build_random_grid(self):
        start, end = self.grid[0][0], self.grid[self.width - 1][self.height - 1]
        while start != end:
