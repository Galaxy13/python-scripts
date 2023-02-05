from functools import wraps

def reversed_dec(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        return func(*args[::-1], **kwargs)

    return wrapped
