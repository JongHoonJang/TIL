T = int(input())
for t in range(T):
    n = int(input())
    res = []
    while n > 0:
        res.append(n % 2)
        n //= 2

    for i in range(len(res)):
        if res[i] == 1:
            print(i,end=' ')
    