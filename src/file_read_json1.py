import json

with open("test1.json") as handle:
    data = json.load(handle)

print(type(data))
print(data)
print(data["GENE"])
