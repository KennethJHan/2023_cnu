data = list()
with open("test.tsv") as handle:
    header = handle.readline().strip().split("\t")
    for line in handle:
        row = line.strip().split("\t")
        data.append(dict(zip(header, row)))

data_sorted = sorted(data, key=lambda x: float(x["VALUE"]), reverse=True)
for row in data_sorted:
    print(row)
