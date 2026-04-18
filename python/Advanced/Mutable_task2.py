# Write a function showing why default mutable arguments are dangerous.
# ❌ Problem: Mutable Default Argument Bug
def add_item(item, items=[]):  # ❗ mutable default
    items.append(item)
    return items


print(add_item("apple"))
print(add_item("banana"))
print(add_item("cherry"))

# ✅ Fix: Use None as Default
def add_item(item, items=None):
    if items is None:
        items = []  # create new list each time
    items.append(item)
    return items


print(add_item("apple"))
print(add_item("banana"))
print(add_item("cherry"))