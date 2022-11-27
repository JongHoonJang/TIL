def BFS(si, sj):
    queue = [(si, sj)]
    c = 0
    while queue:
        y, x = queue.pop(0)
        if not visited[y][x]:
            visited[y][x] = 1
            c += 1
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny, nx = dy + y, dx + x
            if 0 <= ny < M and 0 <= nx < N:
                if arr[ny][nx] == 0 and not visited[ny][nx]:
                    queue.append((ny, nx))
                    visited[ny][nx] = 1
                    arr[ny][nx] = 1
                    c += 1
    else:
        return c


M, N, K = map(int, input().split())
arr = [[0] * N for _ in range(M)]
for k in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            arr[y][x] = 1
visited = [[0] * N for _ in range(M)]
lst = []
for i in range(M):
    for j in range(N):
        if arr[i][j] == 0:
            lst.append(BFS(i, j))
lst.sort()
print(len(lst))
print(*lst)
