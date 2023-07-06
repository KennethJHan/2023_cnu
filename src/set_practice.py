genelist_1 = ["BRAF", "MEN1", "RET", "KRAS", "BRAF"]
genelist_2 = ["MEN1", "PTEN", "KRAS", "TERT", "P53"]

geneset_1 = set(genelist_1)
geneset_2 = set(genelist_2)

all_gene = geneset_1.union(geneset_2)
common_gene = geneset_1.intersection(geneset_2)
gene_a = geneset_1 - geneset_2
gene_b = geneset_2 - geneset_1

print(all_gene)
print(common_gene)
print(gene_a)
print(gene_b)
