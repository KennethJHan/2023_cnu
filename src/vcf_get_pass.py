all_cnt = 0
pass_cnt = 0

with open("sample.vcf") as handle:
    for line in handle:
        if line.startswith("##"):
            continue

        if line.startswith("#"):
            header = line.strip().split("\t")
            filter_idx = header.index("FILTER")
            continue

        row = line.strip().split("\t")
        if row[filter_idx] == "PASS":
            pass_cnt += 1

        all_cnt += 1

print(f"PASS: {pass_cnt}/{all_cnt} ({round(pass_cnt/all_cnt*100, 2)}%)")
