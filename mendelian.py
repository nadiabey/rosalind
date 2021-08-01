def alleles(dom, het, rec):
    orgs = []
    for i in range(0,dom):
        orgs.append(1)
    for i in range(0,het):
        orgs.append(0.5)
    for i in range(0,rec):
        orgs.append(0)
    return orgs

def punnett(l):
    prob = []
    for i in range(len(l)):
        for j in range(len(l)):
            if i != j:
                if l[i] == 1 or l[j] == 1:
                    prob.append(1)
                elif l[i] == 0.5 and l[j] == 0.5:
                    prob.append(0.75)
                elif l[i] == 0.5 and l[j] == 0:
                    prob.append(0.5)
                elif l[i] == 0 and l[j] == 0.5:
                    prob.append(0.5)
                elif l[i] == 0 and l[j] == 0:
                    prob.append(0)
    return prob


def result(l):
    temp = 0
    for x in l:
        temp += x
    ret = temp / len(l)
    return ret

if __name__ == '__main__':
    a = alleles(26,26,28)
    p = punnett(a)
    print(result(p))