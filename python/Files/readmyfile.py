# Convert JSON String ↔ Python
import json

# String to dict
data = json.loads('{"name": "Satya"}')
print(data)
# Dict to string
json_str = json.dumps(data)
print(json_str)