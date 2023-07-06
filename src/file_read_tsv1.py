with open("test.tsv") as handle:
    for line in handle:
        row = line.strip().split("\t")
        print(row)
