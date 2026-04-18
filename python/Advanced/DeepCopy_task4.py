# Implement cloning logic for a nested dictionary with lists.
def clone(data):
    # Base case: immutable types
    if isinstance(data, (int, float, str, bool, type(None))):
        return data

    # Handle list
    if isinstance(data, list):
        return [clone(item) for item in data]

    # Handle dict
    if isinstance(data, dict):
        return {key: clone(value) for key, value in data.items()}

    # Fallback (for unsupported types)
    return data

original = {
    "user": "Alice",
    "skills": ["Python", "React"],
    "projects": [
        {"name": "AI", "tags": ["ML", "DL"]},
        {"name": "Web", "tags": ["Frontend"]}
    ]
}

copied = clone(original)

# Modify copied data
copied["projects"][0]["tags"].append("NLP")

print("Original:", original)
print("Copied  :", copied)

