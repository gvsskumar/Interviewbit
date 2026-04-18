# Lambda with Map()
# Use lambda with map() to square all numbers in a list.
nums = [1,2,3,4,5,6]
res = list(map(lambda x:x**2))
print(res) # [1, 4, 9, 16, 25, 36]

# Use lambda with map() to convert a list of strings to uppercase.
nums = [1, 2, 3, 4, 5]
squared_nums = list(map(lambda x: x**2, nums))
print(squared_nums)

# Use lambda with map() to add two lists element-wise.
list1 = [1,2,3,4]
list2 = [5,6,7,8]
res = list(map(lambda x,y:x+y,list1,list2))
print(res)

# Use lambda with map() to find length of each string in a list.
list3 = ['gvk','satya','kumar']
res3 = list(map(lambda s1:len(s1),list3))
print(res3)

