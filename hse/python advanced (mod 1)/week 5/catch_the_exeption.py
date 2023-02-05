def exception_logger(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs), None
        except (ZeroDivisionError, AssertionError, ArithmeticError) as err:
            return None, type(err)
    return inner