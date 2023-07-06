import gzip

cnt = 0
read_cnt = 0
with gzip.open("sample.fastq.gz", "rt") as handle:
    for line in handle:
        cnt += 1
        if cnt % 4 == 1:
            # header
            read_cnt += 1
        elif cnt % 4 == 2:
            # seq
            pass
        elif cnt % 4 == 3:
            # +
            pass
        elif cnt % 4 == 0:
            # qual
            cnt = 0

print(read_cnt)
