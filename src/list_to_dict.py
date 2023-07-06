l = [3, 1, 1, 2, 0, 0, 2, 3, 3]
d = dict()
for elem in l:
    if elem not in d:
        d[elem] = 0
    d[elem] += 1

print(d)
