# Challenge 2: Custom Multiplier
def multiplier(n):
    def multiply(x):
        return x * n
    return multiply

times3 = multiplier(3)
print(times3(5))  # 15