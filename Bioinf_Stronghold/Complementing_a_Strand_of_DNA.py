from pathlib import Path

FILENAME = Path("../rosalind.txt")


def Complementing_a_Strand_of_DNA(s: str) -> str:
    """
    A -> T
    T -> A
    C -> G
    G -> C
    AAAACCCGGT 
    ACCGGGTTTT
    """
    complement = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    }
    complement_strand = "".join(complement[n] for n in reversed(s))
    return complement_strand


with open(FILENAME, mode="r", encoding="utf-8") as file:
    s = file.read().strip()
print(len(s))
print(Complementing_a_Strand_of_DNA(s))
