# Multiprocessing vs Multithreading
from multiprocessing import Process
import time

def cpu_task():
    count = 0
    for _ in range(10**7):
        count += 1

start = time.time()

p1 = Process(target=cpu_task)
p2 = Process(target=cpu_task)

p1.start()
p2.start()

p1.join()
p2.join()

print("Time:", time.time() - start)