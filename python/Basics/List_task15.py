# Convert a list variable into a tuple.
numbers = [10, 20, 30, 40, 50]

# Using tuple() Function (Most Common)
mytupleValue = tuple(numbers)
print(mytupleValue)

# Using Tuple Packing
mytupleValue1 = (*numbers,)
print(mytupleValue1)