try:
    with open("noname.txt") as handle:
        lines = handle.readlines()

    print(lines)
except FileNotFoundError:
    print("Check your input file")
    
print("# END")
