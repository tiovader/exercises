import re
from itertools import takewhile
from enum import Enum


class Codon(Enum):
    AUG = 'Methionine'
    UUU = UUC = 'Phenylalanine'
    UUA = UUG = 'Leucine'
    UCU = UCC = UCA = UCG = 'Serine'
    UAU = UAC = 'Tyrosine'
    UGU = UGC = 'Cysteine'
    UGG = 'Tryptophan'
    UAA = UAG = UGA = 'STOP'


def proteins(strand: str) -> list[str]:
    return list(
        takewhile(lambda c: c != 'STOP',
                  (Codon[c].value for c in re.findall(r'.{3}', strand))))
