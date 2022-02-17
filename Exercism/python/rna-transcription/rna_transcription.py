def to_rna(dna_strand):
    return ''.join([{'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}.get(i)
                    for i in dna_strand])
