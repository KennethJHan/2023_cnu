l = [3, 1, 1, 2, 0, 0, 2, 3, 3]
max_val = l[0]
min_val = l[0]

for i in range(1, len(l)):
    if l[i] > max_val:
        max_val = l[i]
    if l[i] < min_val:
        min_val = l[i]

print(max_val)
print(min_val)
