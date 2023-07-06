covid_aa = (
    "MFVFLVLLPLVSSQCVNLTTRTQLPPAYTNSFTRGVYYPDKVFRSSVLHSTQDLFLPFFSNVTWFHAIHVSGTN"
    "GTKRFDNPVLPFNDGVYFASTEKSNIIRGWIFGTTLDSKTQSLLIVNNATNVVIKVCEFQFCNDPF"
)

data = dict()

for aa in covid_aa:
    if aa not in data:
        data[aa] = 0

    data[aa] += 1

print(sorted(data.items(), key=lambda x: x[1], reverse=True)[:3])
print(sorted(data.items(), key=lambda x: x[1])[:3])
