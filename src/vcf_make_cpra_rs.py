with open("sample.vcf") as handle:
    for line in handle:
        if line.startswith("##"):
            continue

        if line.startswith("#"):
            header = line.strip().split("\t")
            chrom_idx = header.index("#CHROM")
            pos_idx = header.index("POS")
            id_idx = header.index("ID")
            ref_idx = header.index("REF")
            alt_idx = header.index("ALT")
            continue

        row = line.strip().split("\t")
        rsid = row[id_idx]
        if rsid == ".":
            continue

        chrom = row[chrom_idx]
        pos = row[pos_idx]
        ref = row[ref_idx]
        alts = row[alt_idx].split(",")
        for alt in alts:
            print(f"{chrom}-{pos}-{ref}-{alt}-{rsid}")
