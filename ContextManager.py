from contextlib import contextmanager
@contextmanager
def my_ctx():
    print("enter")
    try:
        yield
    finally:
        print("exit")

with my_ctx():
    print("inside")
