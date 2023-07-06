gene_expr = [3.14, 11.82, 7.44, 1.92]
codon = ["ATG", "GGC", "TGA", "CCT"]

gene_expr.sort()
codon.sort()

print(gene_expr)
print(codon)

gene_expr.sort(reverse=True)
codon.sort(reverse=True)

print(gene_expr)
print(codon)
