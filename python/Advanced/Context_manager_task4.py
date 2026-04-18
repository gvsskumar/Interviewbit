#Implement a context manager for timing code execution.
import time

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self  # optional

    def __exit__(self, exc_type, exc_value, traceback):
        end = time.perf_counter()
        duration = end - self.start
        print(f"Execution time: {duration:.6f} seconds")
with Timer():
    total = sum(range(10_000_000))        