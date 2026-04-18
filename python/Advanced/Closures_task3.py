# Write a closure that maintains a running total.
def running_total():
    total = 0  # enclosed variable

    def add(value):
        nonlocal total  # allows modification of outer variable
        total += value
        return total

    return add


# Usage
counter = running_total()

print(counter(5))   # 5
print(counter(10))  # 15
print(counter(3))   # 18