data_gt = dict()

with open("sample.vcf") as handle:
    for line in handle:
        if line.startswith("##"):
            continue

        if line.startswith("#"):
            header = line.strip().split("\t")
            format_idx = header.index("FORMAT")
            sample_idx = header.index("Sample1")
            continue

        row = line.strip().split("\t")
        frmt = row[format_idx]
        gt_idx = frmt.split(":").index("GT")
        sample_gt = row[sample_idx].split(":")[gt_idx]
        if sample_gt not in data_gt:
            data_gt[sample_gt] = 0

        data_gt[sample_gt] += 1

for gt, cnt in data_gt.items():
    print(f"{gt}: {cnt}")
