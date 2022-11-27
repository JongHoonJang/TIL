def DFS(n, value):
    global res
    if res < value:
        return
    if n == N:
        if res > value:
            res = value
        return
    for i in range(N):
        if arr[n][i] != 0 and not visited[i]:
            visited[i] = 1
            DFS(n + 1, value + arr[n][i])
            visited[i] = 0


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    res = 99999999
    for i in range(N):
        visited = [0] * N
        visited[i] = 1
        DFS(1, arr[0][i])

    print(f'#{t} {res}')
