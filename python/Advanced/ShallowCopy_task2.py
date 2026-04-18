# Identify Bug in Production Code
data = [{"id": 1, "tags": ["a", "b"]}]
backup = data.copy()

backup[0]["tags"].append("c")

print(data)