with open("test.csv") as handle:
    for line in handle:
        row = line.strip().split(",")
        print(row)
