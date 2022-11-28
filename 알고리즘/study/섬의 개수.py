def BFS(ci, cj):
    queue = [(ci, cj)]
    while queue:
        yi, xj = queue.pop(0)
        if not visited[yi][xj]:
            visited[yi][xj] = 1
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]:
            ny, nx = yi + dy, xj + dx
            if 0 <= ny < y and 0 <= nx < x:
                if arr[ny][nx] == 1 and not visited[ny][nx]:
                    queue.append((ny, nx))
                    visited[ny][nx] = 1


while True:
    x, y = map(int, input().split())
    if y == 0 and x == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(y)]
    visited = [[0] * x for _ in range(y)]
    cnt = 0
    for i in range(y):
        for j in range(x):
            if arr[i][j] == 1 and not visited[i][j]:
                BFS(i, j)
                cnt += 1

    print(cnt)