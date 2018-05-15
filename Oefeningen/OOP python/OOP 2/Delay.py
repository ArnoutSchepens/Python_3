
from functools import wraps
from time      import sleep

def delay(sec):

    def decorator(fn):

        @wraps(fn)
        def wrapper(*args, **kwargs):
            print(f"Waiting {sec}s before running {fn.__name__}")
            sleep(sec)
            return fn(*args, **kwargs)
        return wrapper
    return decorator

@delay(3)
def say_hi():
    return "hi"


@delay(1)
def say_yo():
    return "Yo"

print(say_hi())
print(say_yo())
