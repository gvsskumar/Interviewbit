# Check if a key exists in a dictionary variable.
# Using in Operator (Most Common)
person = {"name": "Satya", "age": 28, "city": "Hyderabad"}
key = "age"

if key in person:
    print("Key exists in the dictionary")
else:
    print("Key does not exist")

# Using get() Method
person = {"name": "Satya", "age": 28}

if person.get("age") is not None:
    print("Key exists")    

# Using keys() Method 
person = {"name": "Satya", "age": 28}

if "age" in person.keys():
    print("Key exists")  
    
     