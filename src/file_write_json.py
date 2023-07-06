import json

data = list()
with open("test.csv") as handle:
    header = handle.readline().strip().split(",")
    for line in handle:
        data.append(dict(zip(header, line.strip().split(","))))

with open("test3-1.json", "w") as handle:
    json.dump(data, handle)

with open("test3-2.json", "w") as handle:
    json.dump(data, handle, indent=4)
