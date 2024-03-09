import json

with open("sample-data.json", 'r') as file:
    data = json.load(file)

# Print header
print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<8} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

imdata = data['imdata'] 
for item in imdata:
    item_data = item['l1PhysIf']['attributes']
    # print(item_data)
    dn = item_data["dn"]
    description = item_data["descr"]
    speed = item_data["speed"] 
    mtu = item_data["mtu"]
    print("{:<50} {:<20} {:<8} {:<6}".format(dn, description, speed, mtu))
