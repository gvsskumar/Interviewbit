# Find the second largest number in a list using lambda.
nums = [10, 45, 23, 67, 34]
second_largest = (lambda x: sorted(x)[-2])(nums)
print(second_largest)

# Sort words in a list by length using lambda.
words = ["apple", "kiwi", "banana", "cherry", "fig"]
result = sorted(words, key=lambda x: len(x))
print(result)

#Use lambda to group words by first letter.
from itertools import groupby
words = ["apple", "banana", "avocado", "cherry", "blueberry"]
# First sort by first letter
words.sort(key=lambda x: x[0])
result = {k: list(v) for k, v in groupby(words, key=lambda x: x[0])}
print(result)

#Use lambda to remove duplicates from a list.
nums = [1, 2, 3, 2, 4, 5, 3, 6]
remove_duplicates = lambda x: list(set(x))
result = remove_duplicates(nums)
print(result)

#Use lambda to calculate product of list elements.
from functools import reduce
nums = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, nums)
print(product)