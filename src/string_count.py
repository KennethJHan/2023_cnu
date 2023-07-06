seq1 = "ATGTTATAG"
data = dict()
for base in seq1:
    if base not in data:
        data[base] = 0

    data[base] += 1

print(data)
