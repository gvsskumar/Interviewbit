# Implement a decorator to cache function results (without functools.lru_cache).
from functools import wraps

def cache(func):
    storage = {}  # dictionary to store results

    @wraps(func)
    def wrapper(*args, **kwargs):
        # Create a key from arguments
        key = (args, tuple(sorted(kwargs.items())))

        if key in storage:
            print("Cache hit")
            return storage[key]

        print("Cache miss")
        result = func(*args, **kwargs)
        storage[key] = result
        return result

    return wrapper


# Usage
@cache
def slow_add(a, b):
    print("Computing...")
    return a + b

print(slow_add(2, 3))  # Cache miss
print(slow_add(2, 3))  # Cache hit