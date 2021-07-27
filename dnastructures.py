nucleotides = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}


def reverse(st):
    temp = st[::-1]
    ret = ""
    for x in temp:
        if x in nucleotides.keys():
            ret += nucleotides[x]
    print(ret)
    return ret


if __name__ == '__main__':
    f = open('rosalind_revc.txt', 'r').readlines()[0]
    reverse(f)