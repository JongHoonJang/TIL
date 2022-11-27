N, M = map(int, input().split())
arr = [input() for _ in range(N)]
visited = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == '#':
            pass
        if arr[i][j] == 'O':
            pass
        if arr[i][j] == 'R' or arr[i][j] == 'B':
            pass
