# Convert JSON String ↔ Python
import json

# String to dict
data = json.loads('{"name": "Satya"}')

# Dict to string
json_str = json.dumps(data)