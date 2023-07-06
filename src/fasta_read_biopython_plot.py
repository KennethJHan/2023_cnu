from Bio import SeqIO
import seaborn as sns
import matplotlib.pyplot as plt

record = SeqIO.read("NC_045512.fasta", "fasta")

data = dict()
for base in record.seq:
    if base not in data:
        data[base] = 0

    data[base] += 1

df = {"BASE": [], "COUNT": []}
for base, count in data.items():
    df["BASE"].append(base)
    df["COUNT"].append(count)

sns.barplot(x="BASE", y="COUNT", data=df)
plt.title("NC_045512 BASE COUNT", fontdict={"size": 16})
plt.xlabel("BASE", fontdict={"size": 12})
plt.ylabel("COUNT", fontdict={"size": 12})
plt.savefig("base_barplot.png")
