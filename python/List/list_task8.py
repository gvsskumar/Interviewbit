# Count how many times a specific element appears in a list.
mylist = [2,3,4,5,6,2,4,6,7,8,9,2]
repeatedValues = {}
duplicate = {}
for i in range(len(mylist)):
    if mylist[i] not in repeatedValues:
        repeatedValues[mylist[i]] =1   
        
    else:
        repeatedValues[mylist[i]] += 1
        duplicate[mylist[i]] =repeatedValues[mylist[i]]
print(duplicate)   
# {2: 3, 4: 2, 6: 2}
     
  
#print(mylist.count(2))
 
