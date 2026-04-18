# CPU-bound task example using threading
import threading
import time

def cpu_task(n):
    result = 0
    for i in range(n):
        result += i * i
    print(f"Task finished for {n}")

numbers = [10_000_000, 12_000_000, 14_000_000, 16_000_000]

threads = []

start_time = time.time()
for n in numbers:
    t = threading.Thread(target=cpu_task, args=(n,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

end_time = time.time()
print(f"Threading took {end_time - start_time:.2f} seconds")

# Problem: Due to Python’s GIL, threads don’t run CPU-bound tasks in parallel effectively. You’ll see little speedup.

# Convert to multiprocessing
import multiprocessing
import time

def cpu_task(n):
    result = 0
    for i in range(n):
        result += i * i
    print(f"Task finished for {n}")

numbers = [10_000_000, 12_000_000, 14_000_000, 16_000_000]

processes = []

start_time = time.time()
for n in numbers:
    p = multiprocessing.Process(target=cpu_task, args=(n,))
    processes.append(p)
    p.start()

for p in processes:
    p.join()

end_time = time.time()
print(f"Multiprocessing took {end_time - start_time:.2f} seconds")
