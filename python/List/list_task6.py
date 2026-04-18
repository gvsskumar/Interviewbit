# Flatten a nested list into a single list.
nested_list = [1, [2, 3], [4, 5], 6]

flat_list = []

for item in nested_list:
    if isinstance(item, list):
        for sub_item in item:
            flat_list.append(sub_item)
    else:
        flat_list.append(item)

print(flat_list)

#---------Another Method -2 same problem-----------------#
flat_list = []

for item in nested_list:
    if type(item) is list:   # faster than isinstance
        flat_list.extend(item)
    else:
        flat_list.append(item)

#---------Another Method 3 same problem-----------------#
flat_list = []

for item in nested_list:
    try:
        flat_list.extend(item)
    except TypeError:
        flat_list.append(item)