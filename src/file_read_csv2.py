data = list()
with open("test.csv") as handle:
    header = handle.readline().strip().split(",")
    for line in handle:
        data.append(dict(zip(header, line.strip().split(","))))

for row in data:
    print(row)
