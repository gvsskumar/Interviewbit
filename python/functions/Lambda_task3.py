# Use lambda with filter() to extract even numbers from a list.
list1 = [2,3,4,5,6,8]
res = list(filter(lambda x:x%2==0,list1))
print(res)
# Use lambda with filter() to remove empty strings from a list.
words = ["apple", "", "banana", "", "cherry"]
result = list(filter(lambda x: x != "", words))
print(result)

# Use lambda with filter() to find numbers greater than 50.
nums = [10, 45, 60, 75, 30, 90]
result = list(filter(lambda x: x > 50, nums))
print(result)

# Use lambda with filter() to filter palindromes from a list of strings.
words = ["madam", "hello", "level", "world", "radar"]
result = list(filter(lambda x: x == x[::-1], words))
print(result)

