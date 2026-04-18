# Count how many unique elements are present in a list.
mylist = [2,3,4,5,6,2,4,6,7,8,9,2]
repeatedValues = {}
duplicate = {}
unique = {}
for i in range(len(mylist)):
    if mylist[i] not in repeatedValues:
        repeatedValues[mylist[i]] =1   
        
    else:
        repeatedValues[mylist[i]] += 1
        duplicate[mylist[i]] =repeatedValues[mylist[i]]
for j in (list(repeatedValues)):
    if j not in duplicate.keys():
      unique[j] =1  
        
print(unique)  
# {3: 1, 5: 1, 7: 1, 8: 1, 9: 1}
  
