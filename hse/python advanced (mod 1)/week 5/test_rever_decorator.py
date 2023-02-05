from reversed_decorator import reversed_dec

def check():
    tests_results = []

    @reversed_dec
    def test_func_1(x, y, z=7):
        return f'{x}_{y}_{z}'

    if test_func_1.__name__ != 'test_func_1':
        return '0\tIncorrect name of the decorated function.'

    try:
        tests_results.extend([
            test_func_1(3, 4, 5) == '5_4_3',
            test_func_1(3, 4, z=5) == '4_3_5',
            test_func_1(3, 4) == '4_3_7',
            test_func_1('456', '234') == '234_456_7',
        ])
    except Exception:
        return '0\tFailed test #1. Please try again!'

    @reversed_dec
    def test_func_2(*args, **kwargs):
        args_str = 'x'.join(map(str, args))
        kwargs_str = 'z'.join(map(lambda x: f'{x[1]}<-{x[0]}', sorted(kwargs.items())))
        return f'{args_str}_{kwargs_str}'

    if test_func_2.__name__ != 'test_func_2':
        return '0\tIncorrect name of the decorated function.'

    try:
        tests_results.extend([
            test_func_2(3, 4, z=5) == '4x3_5<-z',
            test_func_2(-903, 4000) == '4000x-903_',
            test_func_2(*range(10)) == '9x8x7x6x5x4x3x2x1x0_',
            test_func_2(*range(-5, 2, 2), **dict(zip(['a', 'n', 't'], [9, 4, 3]))) == '1x-1x-3x-5_9<-az4<-nz3<-t',
        ])
    except Exception:
        return '0\tFailed test #2. Please try again!'

    @reversed_dec
    def test_func_3():
        return 5

    if test_func_3.__name__ != 'test_func_3':
        return '0\tIncorrect name of the decorated function.'

    try:
        if test_func_3() != 5:
            return '0\tFailed test #3. Please try again!'
    except Exception:
        return '0\tFailed test #4. Please try again!'

    # check answers
    for test_idx, test_result in enumerate(tests_results, start=1):
        if test_result is False:
            return f'0\tTest #{test_idx} - incorrect answer. Please try again!'

    return '1\tGreat job! You passed all test cases.'

def test_revdec():
    result, message = check().split('\t')
    assert result == '1', message
    print(message)