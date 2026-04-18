# Find duplicate elements in a list using loops.
my_list = [2,3,5,1,6,7,2,4,6,8,2,9]
duplicates = []
for i in range(len(my_list)):
    for j in range(i+1,len(my_list)):
        if my_list[i] == my_list[j]:
            if my_list[i] not in duplicates:
                duplicates.append(my_list[i])
print(duplicates)  # [2, 6]
          
