class DNA:
    def __init__(self, seq: str, sample_id: int):
        self.seq = seq
        self.sample_id = sample_id

    def get_length(self):
        return len(self.seq)

    def get_reverse_sequence(self):
        return self.seq[::-1]

    def __str__(self):
        return f">{self.sample_id}\n{self.seq}"

    def __add__(self, other):
        return self.seq + other.seq


if __name__ == "__main__":
    dna1 = DNA("ATGTTATAG", 123)
    dna2 = DNA("CCCGGGTTT", 456)
    print(dna1 + dna2)
