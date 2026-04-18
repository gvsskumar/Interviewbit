# Update an existing value in a dictionary variable.
# Using Assignment (Most Common)
person = {"name": "Satya", "age": 28, "city": "Hyderabad"}
person["age"] = 30
print(person)

# Using update() Method
person = {"name": "Satya", "age": 28}
person.update({"age": 30})
print(person)