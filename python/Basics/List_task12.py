# Remove a specific element from a list variable.
numbers = [1,2,3,4,5,6,7,8,9]

# Using remove(value) (Most Common)
numbers.remove(3)
print(numbers) # [1, 2, 4, 5, 6, 7, 8, 9]

# Using pop() (Remove by Index)
numbers.pop() #Default last indix postion removed 
print(numbers) # [1, 2, 4, 5, 6, 7, 8]

# Using List Comprehension
numbers = [x for x in numbers if x!=5]
print(numbers) # [1, 2, 4, 6, 7, 8]

# Using del Keyword index based removed
del numbers[4] # 4th-> index position removed value is 7
print(numbers) # [1, 2, 4, 6, 8]

# remove() → remove by value
# pop() → remove by index
# del → delete by index or slice