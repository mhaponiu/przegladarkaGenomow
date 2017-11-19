from functools import wraps, partial


def drop_exception(func=None, msg="EXCEPTION OCCURED"):
    '''
    decorator caches exception and prints msg:
    usages:
        @drop_exception
        @drop_exception(msg="ANOTHER MESSAGE")
    '''
    if func is None:
        return partial(drop_exception, msg=msg)
    @wraps(func)
    def wrapper(*args, **kwargs):
        def try_except(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception:
                print(msg)
        return try_except(*args, **kwargs)
    return wrapper