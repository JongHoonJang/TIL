def sub(n):
    global cnt
    for i in range(2):
        if tree[i][n]:
            cnt += 1
            j = tree[i][n]
            sub(j)


T = int(input())

for t in range(1, T + 1):
    E, N = map(int, input().split())
    lst = list(map(int, input().split()))
    tree = [[0] * (E + 2) for _ in range(2)]
    cnt = 1
    for i in range(0, 2 * E, 2):
        idx = lst[i]
        data = lst[i + 1]
        if not tree[0][idx]:
            tree[0][idx] = data
        else:
            tree[1][idx] = data
    sub(N)
    print(f'#{t} {cnt}')
