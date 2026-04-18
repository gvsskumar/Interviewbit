# Create a decorator to measure execution time of a function.
import time
from functools import wraps

def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        
        result = func(*args, **kwargs)
        
        end = time.time()
        print(f"{func.__name__} executed in {end - start:.6f} seconds")
        
        return result
    return wrapper


# Usage
@measure_time
def slow_function():
    time.sleep(1)
    return "Done"

slow_function()