# Implement a generator that produces prime numbers indefinitely.
def generate_primes():
    num = 2  # first prime number

    while True:
        is_prime = True

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            yield num

        num += 1


# Usage
gen = generate_primes()

for _ in range(10):
    print(next(gen))