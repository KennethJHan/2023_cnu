contents = [">A_Strain", "ATGCGGAAG", "TCGGGATAG"]
with open("write_sample.txt", "w") as handle:
    handle.write("\n".join(contents))

# with open("write_sample.txt", "w") as handle:
#     handle.write(">A_Strain\n")
#     handle.write("ATGCGGAAG\n")
#     handle.write("TCGGGATAG\n")
