import gzip

cnt = 0
data = {"A": 0, "C": 0, "G": 0, "T": 0}

with gzip.open("sample.fastq.gz", "rt") as handle:
    for line in handle:
        cnt += 1
        if cnt % 4 == 1:
            # header
            pass
        elif cnt % 4 == 2:
            # seq
            for s in line.strip():
                data[s] += 1
        elif cnt % 4 == 3:
            # +
            pass
        elif cnt % 4 == 0:
            # qual
            cnt = 0

for base, count in data.items():
    print(f"{base}: {count}")
