# Find the duplicate element in a list with optimal time complexity.
mylist =  [1, 2, 3, 2, 4, 5, 1]
unique = {}
duplicate = {}
for num in mylist:
    if num in unique:
        unique[num] += 1
        if unique[num] >1:
            duplicate[num] = unique[num]                 
    else:
        unique[num] = 1
print(list(duplicate))

# Method -2
def find_duplicates(nums):
    seen = set()
    duplicates = set()

    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return list(duplicates)


nums = [1, 2, 3, 2, 4, 5, 1]
print(find_duplicates(nums))


