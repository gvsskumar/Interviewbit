# Find the maximum and minimum values in a list variable.
numbers = [6,2,4,8,1,3,9,5]
# MinValue : 1, MaxValue : 9
# Using predefined math function min, max
print(f"MinValue : {min(numbers)}, MaxValue : {max(numbers)}")

# Using a Loop (Interview Logic)
max_val = numbers[0]
min_val = numbers[0]
for num in numbers:
    if num > max_val:
       max_val = num
    if num < min_val:
        min_val = num

print(f"MinValue : {min_val}, MaxValue : {max_val}")

# Using Sort method find list starting ending indexs
numbers.sort()
print(f"MinValue : {numbers[0]}, MaxValue : {numbers[-1]}")


