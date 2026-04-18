arr = [1,2,3,4,5,2,1]

seen = set()
duplicate = set()
for num in arr:
    if num in seen:
        duplicate.add(num)
    else:
        seen.add(num)
print(list(duplicate))        