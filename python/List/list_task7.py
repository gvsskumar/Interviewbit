# Print list elements in reverse order using a loop.
mylist = [2,4,6,8,1,3,5]
for i in range(len(mylist)):
    for j in range(len(mylist)):
        if mylist[i] > mylist[j]:
            temp = mylist[j]
            mylist[j] = mylist[i]
            mylist[i] = temp
print(mylist)
# [8, 6, 5, 4, 3, 2, 1]
