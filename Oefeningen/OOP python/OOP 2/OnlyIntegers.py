
from functools import wraps

def only_ints(fn):
    
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if not all([isinstance(x, int) for x in args]):
            return "Please only invoke with integers"
        return fn(*args)

    return wrapper

@only_ints
def add(x, y):
    return x + y

print(add(1, 2))
print(add("1", "2"))