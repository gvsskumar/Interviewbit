# Challenge 1: Function Execution Timer

import time

def timer(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        print("Time",time.time()-start)
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
slow_function()    