# CPU-bound task: Compute sum of squares (heavy computation)
# I/O-bound task: Simulate file reading (async sleep)

import threading
import multiprocessing
import asyncio
import time

# 2️⃣ CPU-bound Example
import threading
import multiprocessing
import asyncio
import time

# CPU-heavy task
def cpu_task(n):
    result = 0
    for i in range(n):
        result += i*i
    return result

numbers = [10_000_000, 12_000_000, 14_000_000, 16_000_000]

# ---------------- Threading ----------------
start = time.time()
threads = []
for n in numbers:
    t = threading.Thread(target=cpu_task, args=(n,))
    threads.append(t)
    t.start()
for t in threads:
    t.join()
print("Threading (CPU-bound):", time.time() - start)

# ---------------- Multiprocessing ----------------
start = time.time()
processes = []
for n in numbers:
    p = multiprocessing.Process(target=cpu_task, args=(n,))
    processes.append(p)
    p.start()
for p in processes:
    p.join()
print("Multiprocessing (CPU-bound):", time.time() - start)

# 3️⃣ I/O-bound Example
import asyncio

async def io_task(n):
    await asyncio.sleep(1)  # Simulate I/O wait
    return n

async def main():
    numbers = [1,2,3,4]
    results = await asyncio.gather(*(io_task(n) for n in numbers))
    print("Asyncio (I/O-bound) finished:", results)

start = time.time()
asyncio.run(main())
print("Asyncio (I/O-bound) time:", time.time() - start)

# Threading version (I/O-bound):
import threading
import time

def io_task_sync(n):
    time.sleep(1)
    print(f"Task {n} done")

threads = []
start = time.time()
for n in range(4):
    t = threading.Thread(target=io_task_sync, args=(n,))
    threads.append(t)
    t.start()
for t in threads:
    t.join()
print("Threading (I/O-bound):", time.time() - start)