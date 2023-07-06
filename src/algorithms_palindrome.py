import sys


def check_palindrome(s: str):
    return s == s[::-1]


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"#usage: python {sys.argv[0]} [n]")
        sys.exit()

    from algorithms_kmer import make_kmer

    l1 = ["A", "C", "G", "T"]
    l2 = ["A", "C", "G", "T"]
    kmer = make_kmer(l1, l2, int(sys.argv[1]))
    cnt = 0
    for elem in kmer:
        if check_palindrome(elem):
            cnt += 1

    print(cnt)
