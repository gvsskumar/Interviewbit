# Demonstrate a bug caused by shallow copy in nested objects and fix it.
import copy

original = {
    "name": "Alice",
    "skills": ["Python", "React"]
}

shallow = copy.copy(original)

# Modify nested object
shallow["skills"].append("AWS")

print("Original:", original)
print("Shallow :", shallow)

#output
Original: {'name': 'Alice', 'skills': ['Python', 'React', 'AWS']}
Shallow : {'name': 'Alice', 'skills': ['Python', 'React', 'AWS']}

# What Went Wrong?
# copy.copy() creates a shallow copy

#==================✅ Fix: Deep Copy=====================#
import copy

original = {
    "name": "Alice",
    "skills": ["Python", "React"]
}

deep = copy.deepcopy(original)

# Modify nested object
deep["skills"].append("AWS")

print("Original:", original)
print("Deep    :", deep)