# Challenge 2: Infinite Generator
def infiniteCounter():
    count = 0
    while True:
        yield count
        count += 1

gen = infiniteCounter()
print(next(gen))
print(next(gen))
