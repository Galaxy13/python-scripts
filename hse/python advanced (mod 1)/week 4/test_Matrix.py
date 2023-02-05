from matrix import *

def check1():
    '''
    Part 1
    __init__(self, matrix)
    __str__(self)
    '''

    try:
        matrix_data = [
            [1, 2, 3],
            [4, 5, 6],
        ]
        matrix_str = '1\t2\t3\n4\t5\t6'

        matrix = Matrix(matrix_data)
        if matrix.__str__() != matrix_str:
            return '0\tIncorrect method __str__. Please try again!'

        matrix_data[0][1] = -10
        if matrix.__str__() != matrix_str:
            return '0\tMethod __init__ should copy input data. Use deepcopy.'
    except Exception:
        return '0\tFailed test #1. Please try again!'

    try:
        matrix_data = [[1]]
        matrix_str = '1'

        matrix = Matrix(matrix_data)
        if matrix.__str__() != matrix_str:
            return '0\tIncorrect method __str__. Please try again!'
    except Exception:
        return '0\tFailed test #2. Please try again!'

    try:
        matrix_data = [[1, 3, 5]]
        matrix_str = '1\t3\t5'

        matrix = Matrix(matrix_data)
        if matrix.__str__() != matrix_str:
            return '0\tIncorrect method __str__. Please try again!'
    except Exception:
        return '0\tFailed test #3. Please try again!'

    try:
        matrix_data = [[-10], [90]]
        matrix_str = '-10\n90'

        matrix = Matrix(matrix_data)
        if matrix.__str__() != matrix_str:
            return '0\tIncorrect method __str__. Please try again!'
    except Exception:
        return '0\tFailed test #4. Please try again!'

    try:
        matrix_data = [[78, -10], [90, 15]]
        matrix_str = '78\t-10\n90\t15'

        matrix = Matrix(matrix_data)
        if matrix.__str__() != matrix_str:
            return '0\tIncorrect method __str__. Please try again!'
    except Exception:
        return '0\tFailed test #5. Please try again!'

    try:
        matrix_data = [
            [78, -10, 67, 23, 12, 4],
            [-90, -15, 9, 56, -23, 10000],
            [1, -2, -3, 0, 51, 26]
        ]
        matrix_str = '78\t-10\t67\t23\t12\t4\n-90\t-15\t9\t56\t-23\t10000\n1\t-2\t-3\t0\t51\t26'

        matrix = Matrix(matrix_data)
        if matrix.__str__() != matrix_str:
            return '0\tIncorrect method __str__. Please try again!'
    except Exception:
        return '0\tFailed test #6. Please try again!'

    return '1\tGreat job! You passed all test cases.'

def test_check1():
    result, message = check1().split('\t')
    assert result == '1', message
    print(message)

def check2():
    '''
    Part 2
    __eq__(self, other)
    size(self)
    '''

    # Part 2
    try:
        matrix_data = [
            [1, 2, 3],
            [4, 5, 6],
        ]
        if Matrix(matrix_data).size() != (2, 3): return '0\tIncorrect method size. Please try again!'
        if Matrix(matrix_data) != Matrix(matrix_data): return '0\tIncorrect method __eq__. Please try again!'
        try:
            _ = Matrix(matrix_data) == matrix_data
            return '0\tIncorrect method __eq__. Please try again!'
        except TypeError:
            pass
        except Exception:
            return '0\tIncorrect method __eq__. Please try again!'

        matrix_data = [[1]]
        if Matrix(matrix_data).size() != (1, 1): return '0\tIncorrect method size. Please try again!'
        if Matrix(matrix_data) != Matrix(matrix_data): return '0\tIncorrect method __eq__. Please try again!'
        try:
            _ = Matrix(matrix_data) == 5
            return '0\tIncorrect method __eq__. Please try again!'
        except TypeError:
            pass
        except Exception:
            return '0\tIncorrect method __eq__. Please try again!'

        matrix_data = [[1, 3, 5]]
        if Matrix(matrix_data).size() != (1, 3): return '0\tIncorrect method size. Please try again!'
        if Matrix(matrix_data) != Matrix(matrix_data): return '0\tIncorrect method __eq__. Please try again!'
        try:
            _ = Matrix(matrix_data) == '2345678sdfgh'
            return '0\tIncorrect method __eq__. Please try again!'
        except TypeError:
            pass
        except Exception:
            return '0\tIncorrect method __eq__. Please try again!'

        matrix_data = [[-10], [90]]
        if Matrix(matrix_data).size() != (2, 1): return '0\tIncorrect method size. Please try again!'
        if Matrix(matrix_data) != Matrix(matrix_data): return '0\tIncorrect method __eq__. Please try again!'
        try:
            _ = Matrix(matrix_data) == (1, 3, 4)
            return '0\tIncorrect method __eq__. Please try again!'
        except TypeError:
            pass
        except Exception:
            return '0\tIncorrect method __eq__. Please try again!'

        matrix_data = [[78, -10], [90, 15]]
        if Matrix(matrix_data).size() != (2, 2): return '0\tIncorrect method size. Please try again!'
        if Matrix(matrix_data) != Matrix(matrix_data): return '0\tIncorrect method __eq__. Please try again!'
        try:
            _ = Matrix(matrix_data) == {'hello': 1}
            return '0\tIncorrect method __eq__. Please try again!'
        except TypeError:
            pass
        except Exception:
            return '0\tIncorrect method __eq__. Please try again!'

        matrix_data = [
            [78, -10, 67, 23, 12, 4],
            [-90, -15, 9, 56, -23, 10000],
            [1, -2, -3, 0, 51, 26]
        ]
        if Matrix(matrix_data).size() != (3, 6): return '0\tIncorrect method size. Please try again!'
        if Matrix(matrix_data) != Matrix(matrix_data): return '0\tIncorrect method __eq__. Please try again!'
    except Exception:
        return '0\tFailed test #7. Please try again!'

    return '1\tGreat job! You passed all test cases.'


def test_check2():
    result, message = check2().split('\t')
    assert result == '1', message
    print(message)

def check3():
    '''
    Part 3
    __add__(self, other)
    __sub__(self, other)
    '''

    # Part 3
    try:
        if not issubclass(MatrixSizeError, Exception):
            return "0\tMatrixSizeError doesn't inherit Exception"

        matrix_data_1 = [[1, 2, 3], [4, 5, 6]]
        matrix_data_2 = [[7, -8, 2], [-14, 17, -8]]
        matrix_data_add = [[8, -6, 5], [-10, 22, -2]]
        matrix_data_sub = [[-6, 10, 1], [18, -12, 14]]
        if Matrix(matrix_data_1) + Matrix(matrix_data_2) != Matrix(matrix_data_add): return '0\tIncorrect method __add__. Please try again!'
        if Matrix(matrix_data_1) - Matrix(matrix_data_2) != Matrix(matrix_data_sub): return '0\tIncorrect method __sub__. Please try again!'

        try:
            _ = Matrix(matrix_data_1) + 5
            return '0\tIncorrect method __add__. Please try again!'
        except TypeError: pass
        except Exception: return '0\tIncorrect method __add__. Please try again!'

        try:
            _ = Matrix(matrix_data_1) - 5
            return '0\tIncorrect method __sub__. Please try again!'
        except TypeError: pass
        except Exception: return '0\tIncorrect method __sub__. Please try again!'

        matrix_data_1 = [[1]]
        matrix_data_2 = [[3]]
        matrix_data_add = [[4]]
        matrix_data_sub = [[-2]]
        if Matrix(matrix_data_1) + Matrix(matrix_data_2) != Matrix(matrix_data_add): return '0\tIncorrect method __add__. Please try again!'
        if Matrix(matrix_data_1) - Matrix(matrix_data_2) != Matrix(matrix_data_sub): return '0\tIncorrect method __sub__. Please try again!'

        try:
            _ = Matrix(matrix_data_1) + list(range(100))
            return '0\tIncorrect method __add__. Please try again!'
        except TypeError: pass
        except Exception: return '0\tIncorrect method __add__. Please try again!'

        try:
            _ = Matrix(matrix_data_1) - list(range(100))
            return '0\tIncorrect method __sub__. Please try again!'
        except TypeError: pass
        except Exception: return '0\tIncorrect method __sub__. Please try again!'

        matrix_data_1 = [[1, 3, 5]]
        matrix_data_2 = [[-7, 8, 0]]
        matrix_data_add = [[-6, 11, 5]]
        matrix_data_sub = [[8, -5, 5]]
        if Matrix(matrix_data_1) + Matrix(matrix_data_2) != Matrix(matrix_data_add): return '0\tIncorrect method __add__. Please try again!'
        if Matrix(matrix_data_1) - Matrix(matrix_data_2) != Matrix(matrix_data_sub): return '0\tIncorrect method __sub__. Please try again!'

        try:
            _ = Matrix(matrix_data_1) + {'a': 1, 'b': 2}
            return '0\tIncorrect method __add__. Please try again!'
        except TypeError: pass
        except Exception: return '0\tIncorrect method __add__. Please try again!'

        try:
            _ = Matrix(matrix_data_1) - {'a': 1, 'b': 2}
            return '0\tIncorrect method __sub__. Please try again!'
        except TypeError: pass
        except Exception: return '0\tIncorrect method __sub__. Please try again!'

        matrix_data_1 = [[-10], [90]]
        matrix_data_2 = [[10], [-90]]
        matrix_data_add = [[0], [0]]
        matrix_data_sub = [[-20], [180]]
        if Matrix(matrix_data_1) + Matrix(matrix_data_2) != Matrix(matrix_data_add): return '0\tIncorrect method __add__. Please try again!'
        if Matrix(matrix_data_1) - Matrix(matrix_data_2) != Matrix(matrix_data_sub): return '0\tIncorrect method __sub__. Please try again!'

        matrix_1 = Matrix([[-10], [90]])
        matrix_2 = Matrix([[1], [3], [5]])
        try:
            _ = matrix_1 + matrix_2
            return '0\tIncorrect method __add__. Please try again!'
        except MatrixSizeError: pass
        except Exception: return '0\tIncorrect method __add__. Please try again!'

        try:
            _ = matrix_1 - matrix_2
            return '0\tIncorrect method __sub__. Please try again!'
        except MatrixSizeError: pass
        except Exception: return '0\tIncorrect method __sub__. Please try again!'

        matrix_1 = Matrix([[-10], [90]])
        matrix_2 = Matrix([[1, 3]])
        try:
            _ = matrix_1 + matrix_2
            return '0\tIncorrect method __add__. Please try again!'
        except MatrixSizeError: pass
        except Exception: return '0\tIncorrect method __add__. Please try again!'

        try:
            _ = matrix_1 - matrix_2
            return '0\tIncorrect method __sub__. Please try again!'
        except MatrixSizeError: pass
        except Exception: return '0\tIncorrect method __sub__. Please try again!'

        matrix_1 = Matrix([[1, 2, 3], [4, 5, 6]])
        matrix_2 = Matrix([[-7, 8, 0]])
        try:
            _ = matrix_1 + matrix_2
            return '0\tIncorrect method __add__. Please try again!'
        except MatrixSizeError: pass
        except Exception: return '0\tIncorrect method __add__. Please try again!'

        try:
            _ = matrix_1 - matrix_2
            return '0\tIncorrect method __sub__. Please try again!'
        except MatrixSizeError: pass
        except Exception: return '0\tIncorrect method __sub__. Please try again!'

    except Exception:
        return '0\tFailed test #8. Please try again!'

    return '1\tGreat job! You passed all test cases.'

def test_check3():
    result, message = check3().split('\t')
    assert result == '1', message
    print(message)

def check4():
    '''
    Part 4
    __mul__(self, other)
    '''

    # Part 4
    try:
        matrix_1 = Matrix([[1, 2], [4, 5], [7, 8]])
        matrix_2 = Matrix([[-8, 9, 12], [-7, 5, 6]])
        matrix_3 = Matrix([[-22, 19, 24], [-67, 61, 78], [-112, 103, 132]])
        if matrix_1 * matrix_2 != matrix_3:
            return '0\tIncorrect method __mul__. Please try again!'

        matrix_3 = Matrix([[112, 125], [55, 59]])
        if matrix_2 * matrix_1 != matrix_3:
            return '0\tIncorrect method __mul__. Please try again!'

        matrix_1 = Matrix([[6]])
        matrix_2 = Matrix([[7]])
        matrix_3 = Matrix([[42]])
        if matrix_1 * matrix_2 != matrix_3:
            return '0\tIncorrect method __mul__. Please try again!'
        if matrix_2 * matrix_1 != matrix_3:
            return '0\tIncorrect method __mul__. Please try again!'

        matrix_1 = Matrix([[-12345]])
        matrix_2 = Matrix([[0]])
        matrix_3 = Matrix([[0]])
        if matrix_1 * matrix_2 != matrix_3:
            return '0\tIncorrect method __mul__. Please try again!'
        if matrix_2 * matrix_1 != matrix_3:
            return '0\tIncorrect method __mul__. Please try again!'

        matrix_1 = Matrix([[1, 2], [4, 5], [7, 8], [-9, 0]])
        matrix_2 = Matrix([[-8, 9, 12], [-7, 5, 6]])
        matrix_3 = Matrix([[-22, 19, 24], [-67, 61, 78], [-112, 103, 132], [72, -81, -108]])
        if matrix_1 * matrix_2 != matrix_3:
            return '0\tIncorrect method __mul__. Please try again!'

        try:
            _ = matrix_2 * matrix_1
            return '0\tIncorrect method __mul__. Please try again!'
        except MatrixSizeError: pass
        except Exception: return '0\tIncorrect method __mul__. Please try again!'

        try:
            _ = matrix_1 * 5
            return '0\tIncorrect method __mul__. Please try again!'
        except TypeError: pass
        except Exception: return '0\tIncorrect method __mul__. Please try again!'

        try:
            _ = matrix_2 * [5, 4, 6, 1]
            return '0\tIncorrect method __mul__. Please try again!'
        except TypeError: pass
        except Exception: return '0\tIncorrect method __mul__. Please try again!'

        try:
            _ = matrix_3 * {'a': 1, 'b': 2}
            return '0\tIncorrect method __mul__. Please try again!'
        except TypeError: pass
        except Exception: return '0\tIncorrect method __mul__. Please try again!'

        try:
            _ = Matrix([[-12345]]) * Matrix([[-12345], [-12345]])
            return '0\tIncorrect method __mul__. Please try again!'
        except MatrixSizeError: pass
        except Exception: return '0\tIncorrect method __mul__. Please try again!'

    except Exception:
        return '0\tFailed test #9. Please try again!'

    return '1\tGreat job! You passed all test cases.'

def test_check4():
    result, message = check4().split('\t')
    assert result == '1', message
    print(message)

def check5():
    '''
    Part 5
    transpose(self)
    '''

    # Part 5
    try:
        matrix_1 = Matrix([[1, 2], [4, 5], [7, 8]])
        matrix_2 = Matrix([[1, 4, 7], [2, 5, 8]])
        if matrix_1.transpose() != matrix_2:
            return '0\tIncorrect method transpose. Please try again!'

        if matrix_2.transpose() != matrix_1:
            return '0\tIncorrect method transpose. Please try again!'

        if matrix_1.transpose().transpose() != matrix_1:
            return '0\tIncorrect method transpose. Please try again!'

        if matrix_2.transpose().transpose() != matrix_2:
            return '0\tIncorrect method transpose. Please try again!'

        matrix_1 = Matrix([[1, 2], [2, 1]])
        if matrix_1.transpose() != matrix_1:
            return '0\tIncorrect method transpose. Please try again!'

        if matrix_1.transpose().transpose() != matrix_1:
            return '0\tIncorrect method transpose. Please try again!'

        matrix_1 = Matrix([[100]])
        if matrix_1.transpose() != matrix_1:
            return '0\tIncorrect method transpose. Please try again!'

        if matrix_1.transpose().transpose() != matrix_1:
            return '0\tIncorrect method transpose. Please try again!'

    except Exception:
        return '0\tFailed test #10. Please try again!'

    return '1\tGreat job! You passed all test cases.'

def test_check5():
    result, message = check5().split('\t')
    assert result == '1', message
    print(message)

def check6():
    '''
    Part 6
    tr(self)
    det(self)
    '''

    # Part 6
    try:
        # tr
        matrix = Matrix([[1, 2], [4, 5], [7, 8]])
        try:
            _ = matrix.tr()
            return '0\tIncorrect method tr. Please try again!'
        except MatrixSizeError: pass
        except Exception: return '0\tIncorrect method tr. Please try again!'

        try:
            _ = matrix.transpose().tr()
            return '0\tIncorrect method tr. Please try again!'
        except MatrixSizeError: pass
        except Exception: return '0\tIncorrect method tr. Please try again!'

        matrix = Matrix([[1, 2], [4, 5]])
        if matrix.tr() != 6:
            return '0\tIncorrect method transpose. Please try again!'

        if matrix.transpose().tr() != 6:
            return '0\tIncorrect method transpose. Please try again!'

        matrix = Matrix([[15]])
        if matrix.tr() != 15:
            return '0\tIncorrect method transpose. Please try again!'

        if matrix.transpose().tr() != 15:
            return '0\tIncorrect method transpose. Please try again!'

        matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        if matrix.tr() != 15:
            return '0\tIncorrect method transpose. Please try again!'

        if matrix.transpose().tr() != 15:
            return '0\tIncorrect method transpose. Please try again!'

        # det
        matrix = Matrix([[1, 2], [4, 5], [7, 8]])
        try:
            _ = matrix.det()
            return '0\tIncorrect method det. Please try again!'
        except MatrixSizeError: pass
        except Exception: return '0\tIncorrect method det. Please try again!'

        matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        if matrix.det() != 0:
            return '0\tIncorrect method det. Please try again!'

        matrix = Matrix([[0]])
        if matrix.det() != 0:
            return '0\tIncorrect method det. Please try again!'

        matrix = Matrix([[7]])
        if matrix.det() != 7:
            return '0\tIncorrect method det. Please try again!'

        matrix = Matrix([[1, 90], [-7, 6]])
        if matrix.det() != 636:
            return '0\tIncorrect method det. Please try again!'

        matrix = Matrix([[98, -4, -7], [0, 23, 87], [-87, 6, 1]])
        if matrix.det() != -32633:
            return '0\tIncorrect method det. Please try again!'

        matrix = Matrix([[3, -9, 0, -6], [7, 4, 1, 8], [9, 12, -21, 8], [9, 7, -5, 2]])
        if matrix.det() != 12816:
            return '0\tIncorrect method det. Please try again!'

    except Exception:
        return '0\tFailed test #11. Please try again!'

    return '1\tGreat job! You passed all test cases.'

def test_check6():
    result, message = check6().split('\t')
    assert result == '1', message
    print(message)