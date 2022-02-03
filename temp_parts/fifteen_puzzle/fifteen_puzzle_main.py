"""
Loyd's Fifteen puzzle - solver and visualizer
Note that solved configuration has the blank (zero) tile in upper left
Use the arrows key to swap this tile with its neighbors
"""

import poc_fifteen_gui


class Puzzle:
    """
    Class representation for the Fifteen puzzle
    """

    def __init__(self, puzzle_height, puzzle_width, initial_grid=None):
        """
        Initialize puzzle with default height and width
        Returns a Puzzle object
        """
        self._height = puzzle_height
        self._width = puzzle_width
        self._grid = [[col + puzzle_width * row
                       for col in range(self._width)]
                      for row in range(self._height)]

        if initial_grid != None:
            for row in range(puzzle_height):
                for col in range(puzzle_width):
                    self._grid[row][col] = initial_grid[row][col]

    def __str__(self):
        """
        Generate string representaion for puzzle
        Returns a string
        """
        ans = ""
        for row in range(self._height):
            ans += str(self._grid[row])
            ans += "\n"
        return ans

    #####################################
    # GUI methods

    def get_height(self):
        """
        Getter for puzzle height
        Returns an integer
        """
        return self._height

    def get_width(self):
        """
        Getter for puzzle width
        Returns an integer
        """
        return self._width

    def get_number(self, row, col):
        """
        Getter for the number at tile position pos
        Returns an integer
        """
        return self._grid[row][col]

    def set_number(self, row, col, value):
        """
        Setter for the number at tile position pos
        """
        self._grid[row][col] = value

    def clone(self):
        """
        Make a copy of the puzzle to update during solving
        Returns a Puzzle object
        """
        new_puzzle = Puzzle(self._height, self._width, self._grid)
        return new_puzzle

    ########################################################
    # Core puzzle methods

    def current_position(self, solved_row, solved_col):
        """
        Locate the current position of the tile that will be at
        position (solved_row, solved_col) when the puzzle is solved
        Returns a tuple of two integers
        """
        solved_value = (solved_col + self._width * solved_row)

        for row in range(self._height):
            for col in range(self._width):
                if self._grid[row][col] == solved_value:
                    return (row, col)
        assert False, "Value " + str(solved_value) + " not found"

    def update_puzzle(self, move_string):
        """
        Updates the puzzle state based on the provided move string
        """
        zero_row, zero_col = self.current_position(0, 0)
        for direction in move_string:
            if direction == "l":
                assert zero_col > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col - 1]
                self._grid[zero_row][zero_col - 1] = 0
                zero_col -= 1
            elif direction == "r":
                assert zero_col < self._width - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col + 1]
                self._grid[zero_row][zero_col + 1] = 0
                zero_col += 1
            elif direction == "u":
                assert zero_row > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row - 1][zero_col]
                self._grid[zero_row - 1][zero_col] = 0
                zero_row -= 1
            elif direction == "d":
                assert zero_row < self._height - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row + 1][zero_col]
                self._grid[zero_row + 1][zero_col] = 0
                zero_row += 1
            else:
                assert False, "invalid direction: " + direction

    ##################################################################
    # Phase one methods

    def lower_row_invariant(self, target_row, target_col):
        """
        Check whether the puzzle satisfies the specified invariant
        at the given position in the bottom rows of the puzzle (target_row > 1)
        Returns a boolean
        """
        if target_row == self._height - 1 and target_col == self._width - 1 and self._grid[target_row][target_col] == 0:
            return True
        elif self._grid[target_row][target_col] != 0:
            return False
        for row_idx in range(target_row, self._height):
            if row_idx == target_row:
                for col_idx in range(target_col + 1, self._width):
                    if self._grid[row_idx][col_idx] != col_idx + self._width * row_idx:
                        return False
            else:
                for col_idx in range(self._width):
                    if self._grid[row_idx][col_idx] != col_idx + self._width * row_idx:
                        return False
        return True

    def solve_interior_tile(self, target_row, target_col):
        """
        Place correct tile at target position
        Updates puzzle and returns a move string
        """
        string_of_moves = ''
        curr_pos = self.current_position(target_row, target_col)
        zero_pos = list(self.current_position(0, 0))
        if zero_pos[0] > curr_pos[0]:
            while zero_pos[0] > curr_pos[0]:
                self.update_puzzle('u')
                string_of_moves += 'u'
                zero_pos[0] -= 1
        elif zero_pos[0] < curr_pos[0]:
            while zero_pos[0] < curr_pos[0]:
                self.update_puzzle('d')
                string_of_moves += 'd'
                zero_pos[0] += 1

        if zero_pos[1] > curr_pos[1]:
            while zero_pos[1] > curr_pos[1]:
                self.update_puzzle('l')
                string_of_moves += 'l'
                zero_pos[1] -= 1
        elif zero_pos[1] < curr_pos[1]:
            while zero_pos[1] < curr_pos[1]:
                self.update_puzzle('r')
                string_of_moves += 'r'
                zero_pos[1] += 1

        pattern_down = 'druld'
        pattern_left = 'drrul'
        pattern_zero_to_left = 'dllu'
        if zero_pos[1] > curr_pos[1]:
            self.update_puzzle(pattern_zero_to_left)
            string_of_moves += pattern_zero_to_left
        while self.current_position(target_row, target_col)[1] < target_col:
            string_of_moves += pattern_left
            self.update_puzzle(pattern_left)
        while self.current_position(target_row, target_col)[0] < target_row:
            self.update_puzzle(pattern_down)
            string_of_moves += pattern_down

        return string_of_moves

    def solve_col0_tile(self, target_row):
        """
        Solve tile in column zero on specified row (> 1)
        Updates puzzle and returns a move string
        """
        string_of_moves = ''
        curr_pos = self.current_position(target_row, 0)
        zero_pos = list(self.current_position(0, 0))
        if self.current_position(target_row, 0)[0] == target_row - 1 and zero_pos == [target_row, 0]:
            self.update_puzzle('u')
            string_of_moves += 'u'
            zero_pos[0] -= 1
            while zero_pos[1] < self._width - 1:
                self.update_puzzle('r')
                zero_pos[1] += 1
                string_of_moves += 'r'
            return string_of_moves
        if zero_pos[0] > curr_pos[0]:
            while zero_pos[0] > curr_pos[0]:
                self.update_puzzle('u')
                string_of_moves += 'u'
                zero_pos[0] -= 1
        elif zero_pos[0] < curr_pos[0]:
            while zero_pos[0] < curr_pos[0]:
                self.update_puzzle('d')
                string_of_moves += 'd'
                zero_pos[0] += 1

        if zero_pos[1] > curr_pos[1]:
            while zero_pos[1] > curr_pos[1]:
                self.update_puzzle('l')
                string_of_moves += 'l'
                zero_pos[1] -= 1
        elif zero_pos[1] < curr_pos[1]:
            while zero_pos[1] < curr_pos[1]:
                self.update_puzzle('r')
                string_of_moves += 'r'
                zero_pos[1] += 1
        if zero_pos[1] == 0:
            self.update_puzzle('rd')

        pattern_right = 'ldrul'
        pattern_left = 'dllur'
        pattern_down = 'dlurd'
        pattern_3x2 = 'ulldruldrdlurdluurddlur'
        if self.current_position(target_row, 0)[1] < 1:
            self.update_puzzle(pattern_right)
            string_of_moves += pattern_right
        else:
            while self.current_position(target_row, 0)[1] > 1:
                self.update_puzzle(pattern_left)
                string_of_moves += pattern_left
        while self.current_position(target_row, 0)[0] < target_row - 1:
            self.update_puzzle(pattern_down)
            string_of_moves += pattern_down
        self.update_puzzle(pattern_3x2)
        string_of_moves += pattern_3x2
        while self.current_position(0, 0)[1] < self._width - 1:
            self.update_puzzle('r')
            string_of_moves += 'r'
        return string_of_moves

    #############################################################
    # Phase two methods

    def row0_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row zero invariant
        at the given column (col > 1)
        Returns a boolean
        """
        if self._grid[0][target_col] != 0 or self._grid[1][target_col] != target_col + self._width:
            return False
        temp_puzzle = self.clone()
        temp_puzzle.set_number(1, target_col, 0)
        return temp_puzzle.row1_invariant(target_col)

    def row1_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row one invariant
        at the given column (col > 1)
        Returns a boolean
        """
        if self._grid[1][target_col] != 0:
            return False
        for col_idx in range(target_col + 1, self._width):
            for row_idx in range(0, 2):
                if self._grid[row_idx][col_idx] != col_idx + self._width * row_idx:
                    return False
        temp_puzzle = self.clone()
        temp_puzzle.set_number(1, self._width - 1, 0)
        return temp_puzzle.lower_row_invariant(1, self._width - 1)

    def solve_row0_tile(self, target_col):
        """
        Solve the tile in row zero at the specified column
        Updates puzzle and returns a move string
        """
        string_of_moves = ''
        curr_pos = self.current_position(0, target_col)
        zero_pos = list(self.current_position(0, 0))

        if zero_pos[1] > curr_pos[1]:
            while zero_pos[1] > curr_pos[1]:
                self.update_puzzle('l')
                string_of_moves += 'l'
                zero_pos[1] -= 1
        elif zero_pos[1] < curr_pos[1]:
            while zero_pos[1] < curr_pos[1]:
                self.update_puzzle('r')
                string_of_moves += 'r'
                zero_pos[1] += 1

        if zero_pos[0] > curr_pos[0]:
            while zero_pos[0] > curr_pos[0]:
                self.update_puzzle('u')
                string_of_moves += 'u'
                zero_pos[0] -= 1
        elif zero_pos[0] < curr_pos[0]:
            while zero_pos[0] < curr_pos[0]:
                self.update_puzzle('d')
                string_of_moves += 'd'
                zero_pos[0] += 1
        if zero_pos[0] != self.current_position(0, target_col)[0]:
            self.update_puzzle('rul')
            string_of_moves += 'rul'

        pattern_right = 'drrul'
        pattern_down = 'druld'
        pattern_2x3 = 'urdlurrdluldrruld'
        if self.current_position(0, target_col)[1] == target_col:
            self.update_puzzle('d')
            return string_of_moves + 'd'
        while self.current_position(0, target_col)[1] < target_col - 1:
            self.update_puzzle(pattern_right)
            string_of_moves += pattern_right
        if self.current_position(0, target_col)[0] < 1:
            self.update_puzzle(pattern_down)
            string_of_moves += pattern_down
        self.update_puzzle(pattern_2x3)
        string_of_moves += pattern_2x3
        return string_of_moves

    def solve_row1_tile(self, target_col):
        """
        Solve the tile in row one at the specified column
        Updates puzzle and returns a move string
        """
        string_of_moves = ''
        curr_pos = self.current_position(1, target_col)
        zero_pos = list(self.current_position(0, 0))
        if zero_pos[0] > curr_pos[0]:
            while zero_pos[0] > curr_pos[0]:
                self.update_puzzle('u')
                string_of_moves += 'u'
                zero_pos[0] -= 1
        elif zero_pos[0] < curr_pos[0]:
            while zero_pos[0] < curr_pos[0]:
                self.update_puzzle('d')
                string_of_moves += 'd'
                zero_pos[0] += 1

        if zero_pos[1] > curr_pos[1]:
            while zero_pos[1] > curr_pos[1]:
                self.update_puzzle('l')
                string_of_moves += 'l'
                zero_pos[1] -= 1
        elif zero_pos[1] < curr_pos[1]:
            while zero_pos[1] < curr_pos[1]:
                self.update_puzzle('r')
                string_of_moves += 'r'
                zero_pos[1] += 1
        if zero_pos[0] != self.current_position(1, target_col)[0]:
            self.update_puzzle('ld')
            string_of_moves += 'ld'

        pattern_left = 'urrdl'
        pattern_down = 'druld'
        if self.current_position(1, target_col)[0] < 1:
            self.update_puzzle(pattern_down)
            string_of_moves += pattern_down
        while self.current_position(1, target_col)[1] < target_col:
            self.update_puzzle(pattern_left)
            string_of_moves += pattern_left
        self.update_puzzle('ur')
        string_of_moves += 'ur'
        return string_of_moves

    ###########################################################
    # Phase 3 methods

    def solve_2x2(self):
        """
        Solve the upper left 2x2 part of the puzzle
        Updates the puzzle and returns a move string
        """
        string_of_moves = ''
        while self.current_position(0, 0)[0] != 0:
            self.update_puzzle('u')
            string_of_moves += 'u'
        while self.current_position(0, 0)[1] != 0:
            self.update_puzzle('l')
            string_of_moves += 'l'

        while not self.row0_invariant(0) and not self.row1_invariant(0):
            self.update_puzzle('drul')
            string_of_moves += 'drul'
        return string_of_moves

    def solve_puzzle(self):
        """
        Generate a solution string for a puzzle
        Updates the puzzle and returns a move string
        """
        pass

            ############################################################
    # Helper methods
    # def search_tile(self, target_row, target_col):
    #     string_of_moves = ''
    #     curr_pos = self.current_position(target_row, 0)
    #     zero_pos = list(self.current_position(0, 0))
    #     if zero_pos[0] > curr_pos[0]:
    #         while zero_pos[0] > curr_pos[0]:
    #             self.update_puzzle('u')
    #             string_of_moves += 'u'
    #             zero_pos[0] -= 1
    #     elif zero_pos[0] < curr_pos[0]:
    #         while zero_pos[0] < curr_pos[0]:
    #             self.update_puzzle('d')
    #             string_of_moves += 'd'
    #             zero_pos[0] += 1
    #
    #     if zero_pos[1] > curr_pos[1]:
    #         while zero_pos[1] > curr_pos[1]:
    #             self.update_puzzle('l')
    #             string_of_moves += 'l'
    #             zero_pos[1] -= 1
    #     elif zero_pos[1] < curr_pos[1]:
    #         while zero_pos[1] < curr_pos[1]:
    #             self.update_puzzle('r')
    #             string_of_moves += 'r'
    #             zero_pos[1] += 1
    #
    #     return string_of_moves, zero_pos, curr_pos


# Start interactive simulation
poc_fifteen_gui.FifteenGUI(Puzzle(4, 4))

# board = Puzzle(3, 3, [[4, 3, 2], [1, 0, 5], [6, 7, 8]])
# print(board.current_position(0, 2))
# print(board.row0_invariant(0))
# print(board.solve_interior_tile(2, 2))
# print(board.solve_col0_tile(3))
# # print(board.solve_row0_tile(2))
# print(board.solve_2x2())
# poc_fifteen_gui.FifteenGUI()
