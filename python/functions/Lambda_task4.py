# Sort a list of numbers using lambda as key.
nums = [5, 2, 9, 1, 7]
res = sorted(nums,key=lambda x:x)
print(res)

# Sort a list of tuples by second element using lambda.
data = [(1, 3), (2, 1), (4, 2), (3, 5)]
result = sorted(data, key=lambda x: x[1])
print(result)

#Sort dictionary items by value using lambda.
data = {"a": 3, "b": 1, "c": 2}
result = sorted(data.items(), key=lambda x: x[1])
print(result)

#Sort a list of dictionaries by age field using lambda.
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]
result = sorted(people, key=lambda x: x["age"])
print(result)
