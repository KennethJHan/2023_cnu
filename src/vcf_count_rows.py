row_cnt = 0

with open("sample.vcf") as handle:
    for line in handle:
        if line.startswith("#"):
            continue

        row_cnt += 1

print(row_cnt)
