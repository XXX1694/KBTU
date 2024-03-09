import json

with open('sample-data.json', 'r') as file:
    data = json.load(file)

# new_json = json.dumps(data, indent=2, sort_keys=True)
# print(new_json)
    
# print(data.items())
    
with open('smple-data2.json', 'w') as file:
    json.dump(data, file, sort_keys=True, indent=10)