nucleotides = {"A": 0, "C": 0, "G": 0, "T": 0}


def count(file):
    for x in file:
        if x in nucleotides.keys():
            nucleotides[x] += 1
    return nucleotides


if __name__ == '__main__':
    file = open('/Users/nadiabey/PycharmProjects/rosalind/rosalind_dna.txt', 'r').readlines()[0]
    count(file)
    print(nucleotides['A'], nucleotides['C'], nucleotides['G'], nucleotides['T'])
