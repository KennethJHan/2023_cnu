import sys


def make_kmer(l1: list, l2: list, n: int):
    if n == 1:
        return l2
    ltmp = list()
    for base1 in l1:
        for base2 in l2:
            ltmp.append(base1 + base2)

    return make_kmer(l1, ltmp, n - 1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"#usage: python {sys.argv[0]} [n]")
        sys.exit()

    n = int(sys.argv[1])
    l1 = ["A", "C", "G", "T"]
    l2 = ["A", "C", "G", "T"]
    kmer = make_kmer(l1, l2, n)
    print(kmer)

