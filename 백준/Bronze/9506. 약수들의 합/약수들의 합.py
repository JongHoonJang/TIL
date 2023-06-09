while True:
    N = int(input())
    if N == -1:
        break
    else:
        res = []
        for i in range(1, N):
            if N % i == 0:
                res.append(i)
        if sum(res) == N:
            print(N, end=' = ')
            for r in range(len(res)):
                if r == (len(res) - 1):
                    print(res[r])
                else:
                    print(res[r], end=' + ')
        else:
            print(str(N) + ' is NOT perfect.')