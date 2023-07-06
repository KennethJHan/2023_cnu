seq1 = "AGTTTATAG"
for i in range(len(seq1)):
    if seq1[i:i+2] == "TT":
        print(i)
