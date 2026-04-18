# Write a decorator that logs function arguments and return values.
from functools import wraps

def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[CALL] {func.__name__} args={args}, kwargs={kwargs}")
        
        result = func(*args, **kwargs)
        
        print(f"[RETURN] {func.__name__} -> {result}")
        return result

    return wrapper


# Usage
@log_calls
def add(a, b):
    return a + b

add(2, 3)