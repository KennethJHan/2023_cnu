seq = ""
total = 0
with open("NC_045512.fasta") as handle:
    _ = handle.readline()
    for line in handle:
        seq += line.strip()

data = dict()
for base in seq:
    if base not in data:
        data[base] = 0

    data[base] += 1


for base, count in data.items():
    print(f"{base}: {count}")
    total += count

print(f"Total: {total}")
