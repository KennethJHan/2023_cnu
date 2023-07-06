import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--input_gene1", required=True)
parser.add_argument("--input_gene2", required=True)

args = parser.parse_args()
print(f"Gene1: {args.input_gene1}")
print(f"Gene2: {args.input_gene2}")
