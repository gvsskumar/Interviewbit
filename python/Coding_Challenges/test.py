import time

class TokenBucket:
    def __init__(self, capacity, refill_rate):
        self.capacity = capacity          # max tokens
        self.tokens = capacity            # current tokens
        self.refill_rate = refill_rate    # tokens per second
        self.last_refill_time = time.time()

    def allow_request(self):
        current_time = time.time()

        # Step 1: Refill tokens
        elapsed = current_time - self.last_refill_time
        refill_tokens = elapsed * self.refill_rate

        self.tokens = min(self.capacity, self.tokens + refill_tokens)
        self.last_refill_time = current_time

        # Step 2: Check availability
        if self.tokens >= 1:
            self.tokens -= 1
            return True
        return False


# Example usage
bucket = TokenBucket(capacity=5, refill_rate=1)

for i in range(10):
    if bucket.allow_request():
        print("Request allowed")
    else:
        print("Request denied")
    time.sleep(0.3)