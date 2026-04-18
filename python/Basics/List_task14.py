# Check whether a value exists in a list variable.
# Using in Operator (Most Common)
numbers = [10, 20, 30, 40, 50]
print(45 in numbers) # False
print(30 in numbers) # True

# Using not in Operator 
print(45 in numbers) # True
print(30 in numbers) # False

# Using Loop (Interview Logic)
Flag = False
for num in numbers:
    if num == 20: # If value changes like 25 then getting False
        Flag = True
print(Flag) # True       

