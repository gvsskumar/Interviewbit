# Remove duplicates from a list using a set variable.
my_list = [1,2,3,4,5,6,2,4,6]

uniqValues = set()
for num in my_list:
    if num not in uniqValues:
        uniqValues.add(num)
print(uniqValues)        