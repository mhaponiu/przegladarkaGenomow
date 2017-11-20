from functools import wraps

def singleton(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        self = args[0]
        func_name = func.__name__
        _func_name = '_' + func_name
        if getattr(self, _func_name, None):
            return getattr(self, _func_name)
        else:
            setattr(self, _func_name, func(*args, **kwargs))
            return getattr(self, _func_name)
    return wrapper






