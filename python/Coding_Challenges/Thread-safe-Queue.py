# Thread-safe Queue (Blocking + Timeout)
import time
from threading import Lock, Condition
import threading

class ThreadSafeQueue:
    def __init__(self, capacity):
        self.queue = []                 # Internal storage
        self.capacity = capacity       # Max size of queue
        self.lock = Lock()             # Mutex lock
        self.not_empty = Condition(self.lock)  # Wait if empty
        self.not_full = Condition(self.lock)   # Wait if full

    # 🔹 Enqueue with blocking + timeout
    def enqueue(self, item, timeout=None):
        with self.not_full:  # Acquire lock
            start_time = time.time()

            while len(self.queue) == self.capacity:
                # Calculate remaining timeout
                if timeout is not None:
                    remaining = timeout - (time.time() - start_time)
                    if remaining <= 0:
                        raise TimeoutError("Queue is full, enqueue timeout")

                    self.not_full.wait(remaining)
                else:
                    self.not_full.wait()

            # Add item
            self.queue.append(item)

            # Notify one waiting consumer
            self.not_empty.notify()

    # 🔹 Dequeue with blocking + timeout
    def dequeue(self, timeout=None):
        with self.not_empty:  # Acquire lock
            start_time = time.time()

            while len(self.queue) == 0:
                if timeout is not None:
                    remaining = timeout - (time.time() - start_time)
                    if remaining <= 0:
                        raise TimeoutError("Queue is empty, dequeue timeout")

                    self.not_empty.wait(remaining)
                else:
                    self.not_empty.wait()

            # Remove item
            item = self.queue.pop(0)

            # Notify one waiting producer
            self.not_full.notify()

            return item

q = ThreadSafeQueue(capacity=2)

def producer():
    for i in range(5):
        print(f"Producing {i}")
        q.enqueue(i)
        time.sleep(1)

def consumer():
    for _ in range(5):
        item = q.dequeue(timeout=3)
        print(f"Consumed {item}")

t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)

t1.start()
t2.start()

t1.join()
t2.join()        