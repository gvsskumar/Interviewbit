# Write a lambda function to add two numbers.
add = lambda a,b:a+b
print(add(3,5))

# Create a lambda function to check if a number is even.
is_even = lambda n:n%2==0
print(is_even(8)) # True
print(is_even(9)) # False

# Write a lambda function to find square of a number.
square = lambda num:num*num
print(square(3)) # 9

# Create a lambda function to find maximum of two numbers.
findMaxValue = lambda n1,n2:n1 if n1>n2 else n2
print(findMaxValue(3,8))

# Write a lambda function to convert a string to uppercase.
convertUpper = lambda name:name.upper()
print(convertUpper("satya"))

# Lambda with map()
# Use lambda with map() to square all numbers in a list.

