from catch_the_exeption import *

def test_check():
    @exception_logger
    def div(x, y):
        return x / y

    try:
        result, err = div(1, 0)  # return ZeroDivisionError
        if result is None and err is ZeroDivisionError:
            pass
        else:
            return '0\tFailed test #1.1. Please try again!'
    except Exception:
        return '0\tFailed test #1.2. Please try again!'

    try:
        div(1, 0, 6)  # should fail
        return '0\tFailed test #2. Please try again!'
    except TypeError:
        pass
    except Exception:
        return '0\tFailed test #3. Please try again!'

    try:
        div(1, 0, j=6)  # should fail
        return '0\tFailed test #4. Please try again!'
    except TypeError:
        pass
    except Exception:
        return '0\tFailed test #5. Please try again!'

    @exception_logger
    def check_assert(*args, **kwargs):
        assert args[0] == 0
        return '_'.join(map(str, args))

    try:
        if check_assert(0, 3, 5) != ('0_3_5', None):
            return '0\tFailed test #6. Please try again!'
    except Exception:
        return '0\tFailed test #7. Please try again!'

    try:
        if check_assert(*[0, 3, 5]) != ('0_3_5', None):
            return '0\tFailed test #8. Please try again!'
    except Exception:
        return '0\tFailed test #9. Please try again!'

    try:
        result, err = check_assert(1, 3, 5)  # return AssertionError
        if result is None and err is AssertionError:
            pass
        else:
            return '0\tFailed test #10.1. Please try again!'
    except Exception:
        return '0\tFailed test #10.2. Please try again!'

    try:
        result, err = check_assert(*[1, 3, 5])  # return AssertionError
        if result is None and err is AssertionError:
            pass
        else:
            return '0\tFailed test #11.1. Please try again!'
    except Exception:
        return '0\tFailed test #11.2. Please try again!'

    @exception_logger
    def check_arithmetic_error(**kwargs):
        if 'k' in kwargs:
            raise ArithmeticError

        return ','.join(map(lambda x: f'{x[0]}={x[1]}', sorted(kwargs.items())))

    try:
        check_arithmetic_error(5)  # should fail
        return '0\tFailed test #12. Please try again!'
    except TypeError:
        pass
    except Exception:
        return '0\tFailed test #13. Please try again!'

    try:
        result, err = check_arithmetic_error(k=10)  # return ArithmeticError
        if result is None and err is ArithmeticError:
            pass
        else:
            return '0\tFailed test #14.1. Please try again!'
    except Exception:
        return '0\tFailed test #14.2. Please try again!'

    try:
        check_arithmetic_error(1, k=9)  # should fail
        return '0\tFailed test #15. Please try again!'
    except TypeError:
        pass
    except Exception:
        return '0\tFailed test #16. Please try again!'

    try:
        if check_arithmetic_error(fgh=9) != ('fgh=9', None):
            return '0\tFailed test #17. Please try again!'
    except Exception:
        return '0\tFailed test #18. Please try again!'

    try:
        if check_arithmetic_error(fgh=9, eru='3456') != ('eru=3456,fgh=9', None):
            return '0\tFailed test #19. Please try again!'
    except Exception:
        return '0\tFailed test #20. Please try again!'

    return '1\tGreat job! You passed all test cases.'


# result, message = check().split('\t')
# assert result == '1', message
# print(message)