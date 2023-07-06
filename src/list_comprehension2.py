codon = ["ATG", "GGC", "TGA", "CCT"]
codon_new = [x for x in codon if "A" not in x]

print(codon_new)
