#  2. Handling JSON Files Writes
import json

data = {"name": "Satya", "age": 28}

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)