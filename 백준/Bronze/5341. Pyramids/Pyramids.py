while True:
    N = int(input())
    if N == 0:
        break
    else:
        res = 0
        for i in range(1, N + 1):
            res += i
        print(res)