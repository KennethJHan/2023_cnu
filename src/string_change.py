seq1 = "ATGTTATAG"
seq1_new = ""
for s in seq1:
    if s == "A":
        seq1_new += "T"
    elif s == "C":
        seq1_new += "G"
    elif s == "G":
        seq1_new += "C"
    elif s == "T":
        seq1_new += "A"

print("ori:", seq1)
print("new:", seq1_new)
