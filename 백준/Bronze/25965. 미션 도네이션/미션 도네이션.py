T = int(input())
for t in range(T):
    M = int(input())
    arr = []
    res = 0
    for i in range(M):
        arr.append(list(map(int, input().split())))
    k, d, a = map(int, input().split())
    for i in range(M):
        if arr[i][0] * k + arr[i][2] * a - arr[i][1] * d > 0:
            res += (arr[i][0] * k + arr[i][2] * a - arr[i][1] * d)
    print(res)