def to_rna(dna):
    rules = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U',
    }

    # result = ''
    # for nucleotid in dna:
        # result += rules[nucleotid]
    
    # better
    rna = []
    for nucleotid in dna:
        rna.append(rules[nucleotid])   

    return ''.join(rna)


def test_to_rna():
    assert to_rna("C") == "G"
    assert to_rna("G") == "C"
    assert to_rna("T") == "A"
    assert to_rna("A") == "U"
    assert to_rna("ACGTGGTCTTAA") == "UGCACCAGAAUU"


if __name__ == "__main__":
    test_to_rna()
