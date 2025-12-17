import time
from functools import wraps

def timer(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        try:
            return fn(*args, **kwargs)
        finally:
            print(f"{fn.__name__} took {time.perf_counter()-start:.4f}s")
    return wrapper

@timer
def work(n):
    sum(i*i for i in range(n))

work(10_000)
