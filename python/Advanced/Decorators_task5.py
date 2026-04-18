# Build an authentication decorator that checks user roles.
from functools import wraps

def retry(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        attempts = 3

        for attempt in range(1, attempts + 1):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"Attempt {attempt} failed: {e}")
                
                if attempt == attempts:
                    print("All retry attempts failed.")
                    raise
    return wrapper


# Usage
@retry
def unstable_function():
    import random
    if random.random() < 0.7:
        raise ValueError("Random failure")
    return "Success"

print(unstable_function())