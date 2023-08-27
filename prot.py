#!/usr/bin/python3

# Rosalind ID: prot
# Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
# Return: The protein string encoded by s.

def read_input(file):
    with open(file, 'r') as f:
        rna = f.read().strip()
    return rna


def read_table(file):
    r2p = {}
    with open(file, 'r') as f:
        for l in f.readlines():
            k, v = l.split()
            if k not in r2p:
                r2p[k] = v
            else:
                print("Error: this codon has been repeated twice!")
    return r2p


def convert_rna_to_protein(rna, r2p):
    protein = ''
    for i in range(0, len(rna), 3):
        codon = rna[i:i+3]
        if codon in r2p:
            if r2p[codon] == 'Stop':#
                if i != len(rna) - 3:
                    # If we have reached the end of the RNA sequence
                    return print(f"Warning: This RNA produces a truncated protein. \n {protein}")
                else:
                    # If we have found a stop codon mid-sequence
                    return print(protein)
            aa = r2p[codon]
            protein += aa



def main():
    rna = read_input("data/rosalind_prot.txt")
    p2r = read_table("constants/rna_codon_table.txt")
    convert_rna_to_protein(rna, p2r)


if __name__ == "__main__":
    main()
