from complex import Complex

def check1():
    '''
    Part 1
    __init__(self, re, im)
    __str__(self)
    '''

    tests_results = []

    # initialization with positive integer numbers
    try:
        tests_results.extend([
            Complex().__str__() == '0+0i',
            Complex(1).__str__() == '1+0i',
            Complex(2, 3).__str__() == '2+3i',
            Complex(re=4, im=5).__str__() == '4+5i',
            Complex(im=6, re=7).__str__() == '7+6i',
            Complex(im=8).__str__() == '0+8i',
            Complex(re=9).__str__() == '9+0i',
            Complex(10, im=11).__str__() == '10+11i',
        ])
    except Exception:
        return '0\tFailed test #1. Please try again!'

    # initialization with positive and negative integer numbers
    try:
        tests_results.extend([
            Complex(-1).__str__() == '-1+0i',
            Complex(0, -2).__str__() == '0-2i',
            Complex(re=4, im=-5).__str__() == '4-5i',
            Complex(im=-6, re=-7).__str__() == '-7-6i',
            Complex(im=-8).__str__() == '0-8i',
            Complex(re=-9).__str__() == '-9+0i',
            Complex(-0, -0).__str__() == '0+0i',
            Complex(10, im=-11).__str__() == '10-11i',
        ])
    except Exception:
        return '0\tFailed test #2. Please try again!'

    # initialization with float numbers
    try:
        _ = Complex(1.56)
        _ = Complex(-5.89, 3.90)
        _ = Complex(re=0.4, im=-0.75)
        _ = Complex(im=.96, re=7.)
        _ = Complex(im=80.567)
        _ = Complex(re=9456/987)
        _ = Complex(-910.345, im=11/4567)
    except Exception:
        return '0\tFailed test #3. Please try again!'

    # initialization with incorrect types
    try:
        _ = Complex('5.78')
        return '0\tFailed test #4. Please try again!'
    except TypeError: pass
    except Exception: return '0\tFailed test #5. Please try again!'

    try:
        _ = Complex(re='-5.78')
        return '0\tFailed test #6. Please try again!'
    except TypeError: pass
    except Exception: return '0\tFailed test #7. Please try again!'

    try:
        _ = Complex((3, 4))
        return '0\tFailed test #8. Please try again!'
    except TypeError: pass
    except Exception: return '0\tFailed test #9. Please try again!'

    try:
        _ = Complex(3, 4, 7)
        return '0\tFailed test #10. Please try again!'
    except TypeError: pass
    except Exception: return '0\tFailed test #11. Please try again!'

    for test_idx, test_result in enumerate(tests_results, start=1):
        if test_result is False:
            return f'0\tTest #{test_idx} - incorrect answer. Please try again!'

    return '1\tGreat job! You passed all test cases.'


def check2():
    '''
    Part 2
    __add__(self, other)
    __sub__(self, other)
    '''

    # check returned value
    try:
        if not isinstance(Complex() + 5, Complex) \
                or not isinstance(Complex() - 5, Complex) \
                or not isinstance(Complex() + 5.78, Complex) \
                or not isinstance(Complex() - 5.78, Complex) \
                or not isinstance(Complex(1) + Complex(1, 2), Complex) \
                or not isinstance(Complex(5) - Complex(8, 9), Complex):
            '0\tFailed test #1. Please try again!'
    except Exception:
        return '0\tFailed test #2. Please try again!'

    tests_results = []

    # add int
    try:
        tests_results.extend([
            (Complex() + 5).__str__() == '5+0i',
            (Complex(1, 2) + 5).__str__() == '6+2i',
            (Complex(-5) + 5).__str__() == '0+0i',
            (Complex(re=4, im=5) + 0).__str__() == '4+5i',
            (Complex(im=6, re=7) + 3).__str__() == '10+6i',
            (Complex(im=8) + 12).__str__() == '12+8i',
            (Complex(re=9) + 80).__str__() == '89+0i',
            (Complex(10, im=11) + 7).__str__() == '17+11i',
        ])
    except Exception:
        return '0\tFailed test #3. Please try again!'

    # add float
    # Yes, I know that float numbers need to be compared with some margin of error,
    # but in this case I'm neglecting this.
    try:
        tests_results.extend([
            (Complex() + 0.5).__str__() == '0.5+0i',
            (Complex(1, 2) + 5.2).__str__() == '6.2+2i',
            (Complex(re=4, im=5) + 0.25).__str__() == '4.25+5i',
            (Complex(im=6, re=7) + 3.5).__str__() == '10.5+6i',
            (Complex(im=8) + 12.5).__str__() == '12.5+8i',
        ])
    except Exception:
        return '0\tFailed test #4. Please try again!'

    # add Complex
    try:
        tests_results.extend([
            (Complex() + Complex()).__str__() == '0+0i',
            (Complex(1, 2) + Complex(5)).__str__() == '6+2i',
            (Complex(-5) + Complex(5, 5)).__str__() == '0+5i',
            (Complex(re=4, im=5) + Complex(-5, -4)).__str__() == '-1+1i',
            (Complex(im=6, re=7) + Complex(-5, -4)).__str__() == '2+2i',
            (Complex(im=8) + Complex(-5, 4)).__str__() == '-5+12i',
            (Complex(re=9) + Complex(5)).__str__() == '14+0i',
            (Complex(im=11) + Complex(7)).__str__() == '7+11i',
        ])
    except Exception:
        return '0\tFailed test #5. Please try again!'

    # sub int
    try:
        tests_results.extend([
            (Complex() - 5).__str__() == '-5+0i',
            (Complex(1, 2) - 5).__str__() == '-4+2i',
            (Complex(-5) + -5).__str__() == '-10+0i',
            (Complex(re=4, im=5) - 0).__str__() == '4+5i',
            (Complex(im=6, re=7) - 3).__str__() == '4+6i',
            (Complex(im=8) - 12).__str__() == '-12+8i',
            (Complex(re=9) - 80).__str__() == '-71+0i',
            (Complex(10, im=11) - 7).__str__() == '3+11i',
        ])
    except Exception:
        return '0\tFailed test #6. Please try again!'

    # sub float
    try:
        tests_results.extend([
            (Complex() - 0.5).__str__() == '-0.5+0i',
            (Complex(1, 2) - 5.2).__str__() == '-4.2+2i',
            (Complex(re=4, im=5) - 0.5).__str__() == '3.5+5i',
            (Complex(im=6, re=7) - 3.5).__str__() == '3.5+6i',
            (Complex(im=8) - 12.5).__str__() == '-12.5+8i',
        ])
    except Exception:
        return '0\tFailed test #7. Please try again!'

    # sub Complex
    try:
        tests_results.extend([
            (Complex() - Complex()).__str__() == '0+0i',
            (Complex(1, 2) - Complex(5)).__str__() == '-4+2i',
            (Complex(-5) - Complex(5, 5)).__str__() == '-10-5i',
            (Complex(re=4, im=5) - Complex(-5, -4)).__str__() == '9+9i',
            (Complex(im=6, re=7) - Complex(-5, -4)).__str__() == '12+10i',
            (Complex(im=8) - Complex(-5, 4)).__str__() == '5+4i',
            (Complex(re=9) - Complex(5)).__str__() == '4+0i',
            (Complex(im=11) - Complex(7)).__str__() == '-7+11i',
        ])
    except Exception:
        return '0\tFailed test #8. Please try again!'

    # check answers
    for test_idx, test_result in enumerate(tests_results, start=1):
        if test_result is False:
            return f'0\tTest #{test_idx} - incorrect answer. Please try again!'

    # check other types
    try:
        _ = Complex(3, 4) + '56'
        return '0\tFailed test #9. Please try again!'
    except TypeError: pass
    except Exception: return '0\tFailed test #10. Please try again!'

    # check other types
    try:
        _ = Complex(3, 4) - '56'
        return '0\tFailed test #11. Please try again!'
    except TypeError: pass
    except Exception: return '0\tFailed test #12. Please try again!'

    # check other types
    try:
        _ = Complex(3, 4) + [Complex()]
        return '0\tFailed test #13. Please try again!'
    except TypeError: pass
    except Exception: return '0\tFailed test #14. Please try again!'

    # check other types
    try:
        _ = Complex(3, 4) - ['56']
        return '0\tFailed test #15. Please try again!'
    except TypeError: pass
    except Exception: return '0\tFailed test #16. Please try again!'

    # check other types
    try:
        _ = Complex(3, 4) + set()
        return '0\tFailed test #17. Please try again!'
    except TypeError: pass
    except Exception: return '0\tFailed test #18. Please try again!'

    # check other types
    try:
        _ = Complex(3, 4) - dict()
        return '0\tFailed test #19. Please try again!'
    except TypeError: pass
    except Exception: return '0\tFailed test #20. Please try again!'

    return '1\tGreat job! You passed all test cases.'


EPS = 1e-8


def cmp_float_numbers(x, y):
    return abs(x - y) < EPS


def check3():
    '''
    Part 3
    __mul__(self, other)
    __div__(self, other)
    '''

    # check returned value
    try:
        if not isinstance(Complex() * 5, Complex) \
                or not isinstance(Complex() / -5, Complex) \
                or not isinstance(Complex() * -5.78, Complex) \
                or not isinstance(Complex() / 15.78, Complex) \
                or not isinstance(Complex(1) * Complex(-1, 2), Complex) \
                or not isinstance(Complex(-5) / Complex(8, -9), Complex):
            '0\tFailed test #1. Please try again!'
    except Exception:
        return '0\tFailed test #2. Please try again!'

    tests_results = []

    # mul int
    try:
        tests_results.extend([
            (Complex() * 5).__str__() == '0+0i',
            (Complex(1, 2) * 5).__str__() == '5+10i',
            (Complex(-5) * 5).__str__() == '-25+0i',
            (Complex(re=4, im=5) * 0).__str__() == '0+0i',
            (Complex(im=6, re=7) * 3).__str__() == '21+18i',
            (Complex(im=8) * 12).__str__() == '0+96i',
            (Complex(re=9) * 80).__str__() == '720+0i',
            (Complex(10, im=11) * 7).__str__() == '70+77i',
        ])
    except Exception:
        return '0\tFailed test #3. Please try again!'

    # mul float
    try:
        pass
    except Exception:
        tests_results.extend([
            cmp_float_numbers((Complex() * 0.5).re, 0),
            cmp_float_numbers((Complex() * 0.5).im, 0),
            cmp_float_numbers((Complex(1, 2) * 5.2).re, 5.2),
            cmp_float_numbers((Complex(1, 2) * 5.2).im, 10.4),
            cmp_float_numbers((Complex(im=6, re=7) * -0.25).re, -1.75),
            cmp_float_numbers((Complex(re=4, im=5) * -0.25).im, -1.25),
            cmp_float_numbers((Complex(im=8) * 12.5).re, 0),
            cmp_float_numbers((Complex(im=8) * 12.5).im, 100),
        ])
        return '0\tFailed test #4. Please try again!'

    # mul Complex
    try:
        tests_results.extend([
            (Complex() * Complex()).__str__() == '0+0i',
            cmp_float_numbers((Complex(1.3, 2.2) * Complex(5)).re, 6.5),
            cmp_float_numbers((Complex(1.3, 2.2) * Complex(5)).im, 11),
            cmp_float_numbers((Complex(-5) * Complex(5.1, 5.8)).re, -25.5),
            cmp_float_numbers((Complex(-5) * Complex(5.1, 5.8)).im, -29),
            cmp_float_numbers((Complex(re=4.2, im=5) * Complex(-5.9, -4)).re, -4.78),
            cmp_float_numbers((Complex(re=4.2, im=5) * Complex(-5.9, -4)).im, -46.3),
            cmp_float_numbers((Complex(im=6, re=17) * Complex(-0.5, -4)).re, 15.5),
            cmp_float_numbers((Complex(im=6, re=17) * Complex(-0.5, -4)).im, -71),
            cmp_float_numbers((Complex(im=0.85) * Complex(-5, 40)).re, -34),
            cmp_float_numbers((Complex(im=0.85) * Complex(-5, 40)).im, -4.25),
            cmp_float_numbers((Complex(re=91) * Complex(0.5)).re, 45.5),
            cmp_float_numbers((Complex(re=91) * Complex(0.5)).im, 0),
            cmp_float_numbers((Complex(im=11.11) * Complex(7)).re, 0),
            cmp_float_numbers((Complex(im=11.11) * Complex(7)).im, 77.77),
        ])
    except Exception:
        return '0\tFailed test #5. Please try again!'

    # truediv int
    try:
        tests_results.extend([
            cmp_float_numbers((Complex() / 5).re, 0),
            cmp_float_numbers((Complex() / 5).im, 0),
            cmp_float_numbers((Complex(1, 2) / 5).re, 0.2),
            cmp_float_numbers((Complex(1, 2) / 5).im, 0.4),
            cmp_float_numbers((Complex(im=6, re=7) / 2).re, 3.5),
            cmp_float_numbers((Complex(im=6, re=7) / 2).im, 3),
            cmp_float_numbers((Complex(re=4, im=5) / 20).re, 0.2),
            cmp_float_numbers((Complex(re=4, im=5) / 20).im, 0.25),
            cmp_float_numbers((Complex(im=1000) / 12.5).re, 0),
            cmp_float_numbers((Complex(im=1000) / 12.5).im, 80),
        ])
    except Exception:
        return '0\tFailed test #6. Please try again!'

    # truediv float
    try:
        tests_results.extend([
            cmp_float_numbers((Complex() / 5.2345).re, 0),
            cmp_float_numbers((Complex() / 5.8765).im, 0),
            cmp_float_numbers((Complex(1, 2) / 0.2).re, 5),
            cmp_float_numbers((Complex(1, 2) / 0.2).im, 10),
            cmp_float_numbers((Complex(im=6, re=7) / 0.256).re, 27.34375),
            cmp_float_numbers((Complex(im=6, re=7) / 0.256).im, 23.4375),
            cmp_float_numbers((Complex(re=0.004, im=-0.05) / 0.0002).re, 20),
            cmp_float_numbers((Complex(re=0.004, im=-0.05) / 0.0002).im, -250),
        ])
    except Exception:
        return '0\tFailed test #7. Please try again!'

    # truediv Complex
    try:
        tests_results.extend([
            cmp_float_numbers((Complex(1, 2) / Complex(1)).re, 1),
            cmp_float_numbers((Complex(1, 2) / Complex(1)).im, 2),
            cmp_float_numbers((Complex(-10.5, 20.5) / Complex(3, -4)).re, -4.54),
            cmp_float_numbers((Complex(-10.5, 20.5) / Complex(3, -4)).im, 0.78),
            cmp_float_numbers((Complex(im=6, re=7) / Complex(3, -4)).re, -0.12),
            cmp_float_numbers((Complex(im=6, re=7) / Complex(3, -4)).im, 1.84),
            cmp_float_numbers((Complex(re=4, im=5) / Complex(0.3, -0.4)).re, -3.2),
            cmp_float_numbers((Complex(re=4, im=5) / Complex(0.3, -0.4)).im, 12.4),
            cmp_float_numbers((Complex(im=1000) / Complex(-500)).re, 0),
            cmp_float_numbers((Complex(im=1000) / Complex(-500)).im, -2),
        ])
    except Exception:
        return '0\tFailed test #8. Please try again!'

    # check answers
    for test_idx, test_result in enumerate(tests_results, start=1):
        if test_result is False:
            return f'0\tTest #{test_idx} - incorrect answer. Please try again!'

    # check other types
    try:
        _ = Complex(3, 4) * '56'
        return '0\tFailed test #9. Please try again!'
    except TypeError: pass
    except Exception: return '0\tFailed test #10. Please try again!'

    # check other types
    try:
        _ = Complex(3, 4) / '56'
        return '0\tFailed test #11. Please try again!'
    except TypeError: pass
    except Exception: return '0\tFailed test #12. Please try again!'

    # check other types
    try:
        _ = Complex(3, 4) * [Complex()]
        return '0\tFailed test #13. Please try again!'
    except TypeError: pass
    except Exception: return '0\tFailed test #14. Please try again!'

    # check other types
    try:
        _ = Complex(3, 4) / ['56']
        return '0\tFailed test #15. Please try again!'
    except TypeError: pass
    except Exception: return '0\tFailed test #16. Please try again!'

    # check other types
    try:
        _ = Complex(3, 4) * set()
        return '0\tFailed test #17. Please try again!'
    except TypeError: pass
    except Exception: return '0\tFailed test #18. Please try again!'

    # check other types
    try:
        _ = Complex(3, 4) / dict()
        return '0\tFailed test #19. Please try again!'
    except TypeError: pass
    except Exception: return '0\tFailed test #20. Please try again!'

    return '1\tGreat job! You passed all test cases.'

def check4():
    '''
    Part 4
    __eq__(self, other)
    __abs__(self)
    '''

    tests_results = []

    # check __eq__
    try:
        tests_results.extend([
            Complex() == Complex(),
            Complex(re=4, im=5) == Complex(im=5, re=4),
            Complex(2, 5) + 2 == Complex(4, 5),
            Complex(2, 5) * 2 == Complex(4, 10),
            Complex(2, 5) / 2 == Complex(1, 2.5),
            Complex(2, 5) - Complex(2, 5) == Complex(),
            Complex(2, 5) + Complex(-2, -5) == Complex(),
            Complex(2, 5) * 0 == Complex(),
            Complex(-25, 35) + Complex(-10, 5) == Complex(10, 75) - Complex(45, 35),
        ])
    except Exception:
        return '0\tFailed test #1. Please try again!'

    # check __abs__
    try:
        tests_results.extend([
            cmp_float_numbers(abs(Complex()), 0),
            cmp_float_numbers(abs(Complex(1)), 1),
            cmp_float_numbers(abs(Complex(im=-1)), 1),
            cmp_float_numbers(abs(Complex(3, 4)), 5),
            cmp_float_numbers(abs(Complex(-5, 12)), 13),
            cmp_float_numbers(abs(Complex(-2, -1.5)), 2.5),
        ])
    except Exception:
        return '0\tFailed test #2. Please try again!'

    # check answers
    for test_idx, test_result in enumerate(tests_results, start=1):
        if test_result is False:
            return f'0\tTest #{test_idx} - incorrect answer. Please try again!'

    return '1\tGreat job! You passed all test cases.'
