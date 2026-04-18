# Build a rate limiter using closures. 
import time

def rate_limiter(max_calls, period):
    calls = []  # store timestamps

    def allow():
        nonlocal calls
        now = time.time()

        # Remove old calls outside time window
        calls = [t for t in calls if now - t < period]

        if len(calls) < max_calls:
            calls.append(now)
            return True
        else:
            return False

    return allow


# Usage
limit = rate_limiter(3, 5)  # 3 calls per 5 seconds

for i in range(5):
    if limit():
        print("Allowed")
    else:
        print("Blocked")
    time.sleep(1)
    