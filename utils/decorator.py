import timeit
from functools import wraps

def timeit_wrapper(number=100):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            stmt = lambda: func(*args, **kwargs)
            total_time = timeit.timeit(stmt, number=number)
            avg_time = total_time / number
            print(f"[{func.__name__}] Avg time over {number} runs: {avg_time:.6f} sec")
            return func(*args, **kwargs)
        return wrapper
    return decorator
