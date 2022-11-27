def DFS(n):
    global cnt, value
    if n == N:
        cnt += 1

    for i in range(1, 4):
        ni = n + i
        if ni <= N:
            DFS(ni)


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    value = []
    cnt = 0
    DFS(0)
    print(cnt)
