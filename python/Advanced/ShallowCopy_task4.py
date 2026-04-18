# Create a class where shallow copy causes shared state issues.
#❌ Problem: Shared State with Shallow Copy
import copy

class ShoppingCart:
    def __init__(self, user, items=None):
        self.user = user
        self.items = items if items is not None else []  # mutable list

    def add_item(self, item):
        self.items.append(item)

    def __repr__(self):
        return f"{self.user}: {self.items}"


# Original object
cart1 = ShoppingCart("Alice", ["Laptop", "Mouse"])

# Shallow copy
cart2 = copy.copy(cart1)

# Modify copied object
cart2.add_item("Keyboard")

print("Original:", cart1)
print("Shallow :", cart2)
#output:
Original: Alice: ['Laptop', 'Mouse', 'Keyboard']
Shallow : Alice: ['Laptop', 'Mouse', 'Keyboard']

# ✅ Fix 1: Use Deep Copy
cart1 = ShoppingCart("Alice", ["Laptop", "Mouse"])
cart2 = copy.deepcopy(cart1)

cart2.add_item("Keyboard")

print("Original:", cart1)
print("Deep    :", cart2)
#output
Original: Alice: ['Laptop', 'Mouse']
Deep    : Alice: ['Laptop', 'Mouse', 'Keyboard']