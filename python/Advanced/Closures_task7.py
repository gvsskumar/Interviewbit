# Write a closure that mimics private variables.
def create_counter():
    count = 0  # "private" variable

    def increment():
        nonlocal count
        count += 1
        return count

    def get():
        return count

    return increment, get


# Usage
inc, get = create_counter()

print(inc())  # 1
print(inc())  # 2
print(get())  # 2