# Implement a function factory using closures (e.g., multiplier function).
def multiplier(factor):
    def multiply(x):
        return x * factor  # factor is captured (closure)
    return multiply


# Usage
double = multiplier(2)
triple = multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15