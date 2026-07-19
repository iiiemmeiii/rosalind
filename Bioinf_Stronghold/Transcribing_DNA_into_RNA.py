from pathlib import Path

FILENAME = Path("../rosalind.txt")


def transcribing_DNA_into_RNA(s: str) -> str:
    return "".join("U" if n == "T" else n for n in s)
    # return s.replace("T","U")
    


with open(FILENAME, mode="r", encoding="utf-8") as file:
    s = file.read().strip()

print(transcribing_DNA_into_RNA(s))
