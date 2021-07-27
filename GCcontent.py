seqs = {}
prop = {}


def fasta(f):
    for i in range(len(f)):
        for x in f[i]:
            if x[0] == ">":
                id = f[i][1:]
                seqs[id] = f[i+1]
    for x in seqs.keys():
        total = len(seqs[x])
        gc = 0
        for y in seqs[x]:
            if y == 'G' or y == 'C':
                gc += 1
        content = round(float(gc) / float(total) * 100, 6)
        prop[x] = content
    return prop


def greatest(dict):
    name = ""
    num = max(dict.values())
    for x in dict.keys():
        if dict[x] == num:
            name = x
    return name, num


if __name__ == '__main__':
    f = open('rosalind_gc.txt','r').readlines()
    listy = [x[:-1] for x in f]
    fasta(listy)
    print(greatest(prop))