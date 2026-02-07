#Mutable data type : Can be changed after creation (in-place modification)
#Mutable data type : List, Dictionary, Set
# EXAMPLE 1 List
list1 = [1, 2, 3];
list2 = list1;
list1[1] = 10;
print(list1); # [1, 10, 3]
print(list2); # [1, 10, 3]

#Example 2
dict1 = {"name": "John", "age": 30};
dict2 = dict1;
dict1["name"] = "Jane";
print(dict1); # {'name': 'Jane', 'age': 30}
print(dict2); # {'name': 'Jane', 'age': 30}
    
#Example 3
set1 = {1, 2, 3};
set2 = set1;
set1.add(4);
print(set1); # {1, 2, 3, 4}
print(set2); # {1, 2, 3, 4}

