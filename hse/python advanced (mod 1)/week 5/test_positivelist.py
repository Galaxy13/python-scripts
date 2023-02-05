from positive_list import *

def check():
    # check custom exceptions definition
    try:
        NonPositiveError
    except NameError:
        return "0\tNonPositiveError doesn't defined"

    try:
        PositiveList
    except NameError:
        return "0\tPositiveList doesn't defined"

    # check custom exceptions inheritance
    if not issubclass(NonPositiveError, Exception):
        return "0\tNonPositiveError doesn't inherit Exception"

    tested_class = PositiveList()

    # append 1 element
    tested_class.append(4)
    if tested_class != [4]:
        return '0\tFailed test #1. Please try again!'

    # append 2 elements
    tested_class.append(1)
    tested_class.append(7)
    if tested_class != [4, 1, 7]:
        return '0\tFailed test #2. Please try again!'

    # append negative element
    try:
        tested_class.append(-7)
    except NonPositiveError:
        pass
    except Exception:
        return '0\tFailed test #3. Use NonPositiveError exception. Please try again!'

    if tested_class != [4, 1, 7]:
        return '0\tFailed test #4. Please try again!'

    # append 0
    try:
        tested_class.append(0)
    except NonPositiveError:
        pass
    except Exception:
        return '0\tFailed test #5. Use NonPositiveError exception. Please try again!'

    if tested_class != [4, 1, 7]:
        return '0\tFailed test #6. Please try again!'

    # check method len
    if len(tested_class) != 3:
        return '0\tFailed test #7. Please try again!'

    # check list method __iadd__
    tested_class += [5, 0, -9]
    if tested_class != [4, 1, 7, 5, 0, -9]:
        return '0\tFailed test #8. Please try again!'

    # check list method extend
    tested_class.extend([10, -98, 0])
    if tested_class != [4, 1, 7, 5, 0, -9, 10, -98, 0]:
        return '0\tFailed test #9. Please try again!'

    # check function sum
    if sum(tested_class) != -80:
        return '0\tFailed test #10. Please try again!'

    # check list method pop
    tested_class.pop(0)
    if tested_class != [1, 7, 5, 0, -9, 10, -98, 0]:
        return '0\tFailed test #11. Please try again!'

    # append 1 element
    tested_class.append(400)
    if tested_class != [1, 7, 5, 0, -9, 10, -98, 0, 400]:
        return '0\tFailed test #12. Please try again!'

    # append negative element
    try:
        tested_class.append(-67)
    except NonPositiveError:
        pass
    except Exception:
        return '0\tFailed test #13. Use NonPositiveError exception. Please try again!'

    if tested_class != [1, 7, 5, 0, -9, 10, -98, 0, 400]:
        return '0\tFailed test #14. Please try again!'

    # append 0
    try:
        tested_class.append(0)
    except NonPositiveError:
        pass
    except Exception:
        return '0\tFailed test #15. Use NonPositiveError exception. Please try again!'

    if tested_class != [1, 7, 5, 0, -9, 10, -98, 0, 400]:
        return '0\tFailed test #16. Please try again!'

    return '1\tGreat job! You passed all test cases.'

def test_positivelist():
    result, message = check().split('\t')
    assert result == '1', message
    print(message)