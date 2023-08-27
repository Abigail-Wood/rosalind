#!/usr/bin/python3

# Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
# Return: A consensus string and profile matrix for the collection.
# (If several possible consensus strings exist, then you may return any one of them.)

def read_collection(file):
    """ Read in a list a collection of at-most 10 DNA strings of equal length in FASTA format."""
    collection = []
    with open(file, 'r') as f:
        sequence = ''
        for l in f.readlines():
            if l.startswith('>'):
                if sequence:
                    collection.append(sequence)
                    sequence = ''
                continue
            else:
                sequence += l.strip()
        collection.append(sequence)
    assert len(set(len(s) for s in collection)) == 1
    return collection


def create_profile_matrix(collection, n):
    base_counts = {}
    for b in 'ACGT':
        base_counts[b] = n * [0]
    for dna in collection:
        for i, b in enumerate(dna):
            base_counts[b][i] += 1
    return base_counts


def print_output(base_counts):
    for b in 'ACGT':
        print(b + ": " + ' '.join(str(n) for n in base_counts[b]))


def print_consensus(base_counts, n):
    consensus = ''
    for i in range(n):
        consensus += max('ATCG', key=lambda b: base_counts[b][i])
    print(consensus)


def main():
    collection = read_collection("data/rosalind_cons.txt")
    n = len(collection[0])
    base_counts = create_profile_matrix(collection, n)
    print_consensus(base_counts, n)
    print_output(base_counts)


if __name__ == "__main__":
    main()
