from Bio import SeqIO

record = SeqIO.read("NC_045512.fasta", "fasta")
print(record)

total = 0
data = dict()
for base in record.seq:
    if base not in data:
        data[base] = 0

    data[base] += 1


for base, count in data.items():
    print(f"{base}: {count}")
    total += count

print(f"Total: {total}")
