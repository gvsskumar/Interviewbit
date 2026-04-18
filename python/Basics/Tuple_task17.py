# Convert a tuple variable into a list.
my_tuple = (10, 20, 30, 40)
# Using list() Function (Most Common)
my_list = list(my_tuple)
print(my_list) # [10, 20, 30, 40]

#Using List Unpacking
my_list1 = [*my_tuple]
print(my_list1) # [10, 20, 30, 40]