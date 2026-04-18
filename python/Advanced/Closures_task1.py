# Challenge 1: Counter using Closure
def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment
c = counter()
print(c())
print(c())