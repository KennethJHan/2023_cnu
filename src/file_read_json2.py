import json

sum_val = 0

with open("test2.json") as handle:
    data = json.load(handle)

for elem in data:
    sum_val += float(elem["VALUE"])

avr_val = sum_val / len(data)
print(avr_val)
