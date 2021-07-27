"""get the hamming distance (different nucleotides) between strings"""


def differences(st1, st2):
    diff = 0
    l1 = [x for x in st1]
    l2 = [x for x in st2]
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            diff += 1
    return diff


if __name__ == '__main__':
    f = open('rosalind_hamm.txt','r').readlines()
    st1 = f[0]
    st2 = f[1]
    d = differences(st1,st2)
    print(d)