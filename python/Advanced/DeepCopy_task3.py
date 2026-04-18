# Compare behavior of copy.copy() vs copy.deepcopy() using complex objects.
| Feature           | `copy.copy()` | `copy.deepcopy()` |
| ----------------- | ------------- | ----------------- |
| Copy level        | Shallow       | Deep              |
| Nested objects    | Shared        | Fully copied      |
| Performance       | Fast          | Slower            |
| Memory usage      | Low           | High              |
| Safe for mutation | ❌ No          | ✅ Yes             |

# Explanation Shallow Copy
# copy.copy():
# Copies only top-level object (Employee)
# Nested objects (projects, Project, tags) are shared
# So modifying nested data affects both objects

# Explanation Deep Copy
# copy.deepcopy():
# Recursively copies entire object graph
# All nested objects are independent
