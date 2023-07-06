import sys

snp, insertion, deletion = 0, 0, 0

with open("sample.vcf") as handle:
    for line in handle:
        if line.startswith("##"):
            continue

        if line.startswith("#"):
            header = line.strip().split("\t")
            chrom_idx = header.index("#CHROM")
            pos_idx = header.index("POS")
            ref_idx = header.index("REF")
            alt_idx = header.index("ALT")
            continue

        row = line.strip().split("\t")
        chrom = row[chrom_idx]
        pos = row[pos_idx]
        ref = row[ref_idx]
        alts = row[alt_idx].split(",")

        for alt in alts:
            if len(ref) == 1 and len(alt) == 1:
                snp += 1
            elif len(ref) < len(alt):
                insertion += 1
            elif len(ref) > len(alt):
                deletion += 1
            else:
                print(row)
                sys.exit()

print(f"SNP: {snp}")
print(f"INS: {insertion}")
print(f"DEL: {deletion}")
