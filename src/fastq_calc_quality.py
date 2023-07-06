import gzip

cnt = 0
data = {"q20": 0, "q30": 0, "all_score": 0, "qual_count": 0}

with gzip.open("sample.fastq.gz", "rt") as handle:
    for line in handle:
        cnt += 1
        if cnt % 4 == 1:
            # header
            pass
        elif cnt % 4 == 2:
            # seq
            pass
        elif cnt % 4 == 3:
            # +
            pass
        elif cnt % 4 == 0:
            # qual
            for q in line.strip():
                qual = ord(q) - 33
                if qual >= 20:
                    data["q20"] += 1
                if qual >= 30:
                    data["q30"] += 1
                data["all_score"] += qual
                data["qual_count"] += 1
            cnt = 0

print(f"Qual avr: {round(data['all_score'] / data['qual_count'], 2)}")
print(f"Q20(%): {round(data['q20'] / data['qual_count'] * 100, 2)}")
print(f"Q30(%): {round(data['q30'] / data['qual_count'] * 100, 2)}")

