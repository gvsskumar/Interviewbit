# Count how many times a value appears in a tuple.
my_tuple = (10, 20, 30, 20, 40, 20)

# Using count() Method (Most Common)
count_value = my_tuple.count(20)
print(count_value) # 20 value is 3 times are there

# Using Loop (Interview Logic)
count_value1 = 0 
for num in my_tuple:
    if num ==20:
        count_value1 += 1
print(count_value1) # 20 value is 3 times are there