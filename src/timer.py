import time
from functools import wraps


def time_func(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Executed {func.__name__} in {end_time - start_time:.6f}s")
        return result

    return wrapper
