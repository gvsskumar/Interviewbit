# Demonstrate immutability of tuples with mutable elements inside.
# Tuple with Mutable Element (List)
t = (1, 2, [3, 4])

print("Before:", t)

# Modify the list inside tuple
t[2].append(5)

print("After :", t)

# Before: (1, 2, [3, 4])
# After : (1, 2, [3, 4, 5])
