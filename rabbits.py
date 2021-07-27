# recurrence relation: Fn = Fn-1 + Fn-2
# F1 = F2 = 1

def fibonacci(n, k):
    ret = 0
    pairs = []
    for i in range(0,n):
        if i <= 1:
            pairs.append(1)
        else:
            pairs.append(pairs[i-1] + pairs[i-2] + k)
        print('month', i+1, pairs[i])
    for x in pairs:
        ret += x
        print(ret)
    return ret

if __name__ == "__main__":
    fibonacci(5,3)