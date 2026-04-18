# Write a function that calculates the average of numbers with a default empty list.
def calculateAvg(mylist):
    sum = 0
    if len(mylist)>1:
       for num in mylist:
          sum += num
       average = sum/len(mylist)
       return average
    else:
        return "Empty List"
print(calculateAvg([1,2,3,4,5])) 
print(calculateAvg([]))    