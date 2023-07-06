covid_aa = (
    "MFVFLVLLPLVSSQCVNLTTRTQLPPAYTNSFTRGVYYPDKVFRSSVLHSTQDLFLPFFSNVTWFHAIHVSGTN"
    "GTKRFDNPVLPFNDGVYFASTEKSNIIRGWIFGTTLDSKTQSLLIVNNATNVVIKVCEFQFCNDPF"
)

data = dict()

for aa in covid_aa:
    if aa not in data:
        data[aa] = 0

    data[aa] += 1

print(data)