# Write a Python program to group array objects by a property. 
# Input : mylist = [ {name:"A", dept:"IT"}, {name:"B", dept:"HR"}, {name:"C", dept:"IT"} ] 
# Output: { IT: [...], HR: [...] }
mylist = [ {"name":"A", "dept":"IT"}, {"name":"B", "dept":"HR"}, {"name":"C", "dept":"IT"} ]
def Groupbyproperty(mylist):
    result = {}
    for item in mylist:
        dept = item['dept']
        if dept not in result:
            result[dept]= [] 
        result[dept].append(item)
    print(result)

Groupbyproperty(mylist)
# {'IT': [{'name': 'A', 'dept': 'IT'}, {'name': 'C', 'dept': 'IT'}], 'HR': [{'name': 'B', 'dept': 'HR'}]}
