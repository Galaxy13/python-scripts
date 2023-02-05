import copy
from functools import reduce


class MatrixSizeError(Exception):
    pass


def countdet_3(matrix):
    sumdet = sum([reduce(lambda x, y: x * y,
                         [matrix[irow][(lambda icol: (icol + irow) % len(matrix))(icol)] for irow in
                          range(len(matrix))]) for icol in range(len(matrix))])
    subdet = sum([reduce(lambda x, y: x * y,
                         [matrix[irow][(lambda icol: (icol - irow))(icol)] for irow in range(len(matrix))]) for
                  icol in range(len(matrix) - 1, -1, -1)])
    return sumdet - subdet

class Matrix:
    # Part 1
    def __init__(self, matrix):
        if isinstance(matrix, list):
            self.matrix = copy.deepcopy(matrix)
        else:
            raise ValueError('Wrong argument to matrix transform')

    def __str__(self) -> str:
        return '\n'.join(['\t'.join([str(col) for col in row]) for row in self.matrix])

    # Part 2
    def __eq__(self, other) -> bool:
        """
        other: Matrix
        """
        try:
            if other.size() != self.size():
                return False
            else:
                for row1, row2 in zip(self.matrix, other.matrix):
                    if row1 != row2:
                        return False
        except AttributeError:
            raise TypeError("'other' object is not Matrix")
        else:
            return True

    def size(self) -> tuple:
        return len(self.matrix), len(self.matrix[0])

    # Part 3
    def __add__(self, other) -> "Matrix":
        """
        other: Matrix
        """
        try:
            if other.size() != self.size():
                raise MatrixSizeError
        except AttributeError:
            raise TypeError("'other' object is not Matrix")
        else:
            return Matrix([[self.matrix[irow][icol] + other.matrix[irow][icol] for icol in range(len(self.matrix[0]))]
                           for irow in range(len(self.matrix))])

    def __sub__(self, other) -> "Matrix":
        """
        other: Matrix
        """
        try:
            if other.size() != self.size():
                raise MatrixSizeError
        except AttributeError:
            raise TypeError("'other' object is not Matrix")
        else:
            return Matrix([[self.matrix[irow][icol] - other.matrix[irow][icol] for icol in range(len(self.matrix[0]))]
                           for irow in range(len(self.matrix))])

    # Part 4
    def __mul__(self, other) -> "Matrix":
        """
        other: Matrix
        """
        try:
            if other.size()[0] != self.size()[1]:
                raise MatrixSizeError
        except AttributeError:
            raise TypeError("'other' object is not Matrix")
        else:
            return Matrix([[sum(item1 * item2 for item1, item2 in zip(row, col)) for col in zip(*other.matrix)] for row in self.matrix])
    # Part 5
    def transpose(self) -> "Matrix":
        return Matrix([[item for item in col] for col in zip(*self.matrix)])

    # Part 6
    def tr(self) -> float:
        if self.size()[0] == self.size()[1]:
            return sum([self.matrix[index][index] for index in range(len(self.matrix))])
        else:
            raise MatrixSizeError

    def det(self) -> float:
        def recursive_determinant(matrix, mul):
            width = len(matrix)
            if width == 1:
                return mul * matrix[0][0]
            else:
                sign = -1
                answer = 0
                for i in range(width):
                    m = []
                    for j in range(1, width):
                        buff = []
                        for k in range(width):
                            if k != i:
                                buff.append(matrix[j][k])
                        m.append(buff)
                    sign *= -1
                    answer = answer + mul * recursive_determinant(m, sign * matrix[0][i])
            return answer
        if self.size()[0] == self.size()[1]:
            return recursive_determinant(self.matrix, 1)
        else:
            raise MatrixSizeError
