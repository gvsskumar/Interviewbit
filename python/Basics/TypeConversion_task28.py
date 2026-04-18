# Convert a list variable into a set.
# Using Set Method
my_list = [1,2,3,4,5,6]
print(set(my_list)) # {1, 2, 3, 4, 5, 6}

# Using Loop
my_list2 = [1,2,3,1,2,4,5,6,4]
uniqueValues = set()
for num in my_list2:
    if num not in uniqueValues:
        uniqueValues.add(num)
print(uniqueValues) # {1, 2, 3, 4, 5, 6}
       