from time import perf_counter
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        f = func(*args, **kwargs)
        print("The function {} took {:.4f} seconds to execute".format(func.__name__, perf_counter() - start))
        return f
    return wrapper