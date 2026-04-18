# Create a list variable and add a new element to it.
# Create a list variable
numbers = [1, 2, 3, 4]

#Using append(element) (Most Common)
# Add a new element to the list
numbers.append(5)

# Print the updated list
print(numbers)

my_list = ["apple", "banana"]
my_list.append("orange")
print(my_list)

# Using insert(index, value)
numbers.insert(-1,7)
print(numbers)

# Using List Concatenation (+)
numbers = numbers + [8]
print(numbers)

# Using extend()
numbers.extend([9])
print(numbers)

# Using List Unpacking (Pythonic Way)

numbers = [*numbers,10]
print(numbers)

# append() → add one element
# insert() → add at specific index
# extend() → add multiple elements