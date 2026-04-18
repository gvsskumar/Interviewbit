# Write a Python program to group array objects by a property. 
# Input : mylist = [ {name:"A", dept:"IT"}, {name:"B", dept:"HR"}, {name:"C", dept:"IT"} ] 
# Output: { IT: [...], HR: [...] }
mylist = [ {"name":"A", "dept":"IT"}, {"name":"B", "dept":"HR"}, {"name":"C", "dept":"IT"} ]
mylist = [
    {"name": "A", "dept": "IT"},
    {"name": "B", "dept": "HR"},
    {"name": "C", "dept": "IT"}
]

def groupbydrpt(data):
    result = {}

    for item in data:
        dept = item["dept"]

        if dept not in result:
            result[dept] = []

        result[dept].append(item)

    print(result)

groupbydrpt(mylist)