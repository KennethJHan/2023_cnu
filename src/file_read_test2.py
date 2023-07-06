cnt = 1
data = {"odd": [], "even": []}
with open("test.txt") as handle:
    for line in handle:
        if cnt % 2 == 1:
            data["odd"].append(line.strip())
        else:
            data["even"].append(line.strip())
        cnt += 1

print("odd: ", data["odd"])
print("even: ", data["even"])
