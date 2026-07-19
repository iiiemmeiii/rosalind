from pathlib import Path

FILENAME = Path("../rosalind.txt")


def counting_dna(s: str):
    nucleotides = {}
    nucleotides_list = [n for n in s]
    for n in nucleotides_list:
        nucleotides[n] = nucleotides.get(n, 0) + 1
    return " ".join(str(nucleotides[v]) for v in sorted(nucleotides))


with open(FILENAME, mode="r", encoding="utf-8") as file:
    s = file.read().strip()

print(counting_dna(s))
