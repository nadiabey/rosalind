def convert(file):
    st = ""
    for x in file:
        if x == "T":
            st += "U"
        else:
            st += x
    return st


f = open('rosalind_rna.txt','r').readlines()[0]
print(convert(f))