from collections import deque


def BFS(y, x):
    queue = deque()
    queue.append((y, x))
    while queue:
        sy, sx = queue.popleft()
        if not visited[sy][sx]:
            visited[sy][sx] = 1
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny, nx = sy + dy, sx + dx
            if 0 <= ny < N and 0 <= nx < M:
                if arr[ny][nx] > 0 and not visited[ny][nx]:
                    if not visited[ny][nx]:
                        queue.append((ny, nx))
                        visited[ny][nx] = visited[sy][sx] + 1


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
k = 0
while True:
    a = [data[:] for data in arr]
    visited = [[0] * M for _ in range(N)]
    count = 0
    for i in range(1, N):
        for j in range(1, M):
            if a[i][j] > 0 and not visited[i][j]:
                BFS(i, j)
                count += 1
    else:
        if count == 1:
            k += 1
            for i in range(1, N):
                for j in range(1, M):
                    if arr[i][j] > 0:
                        cnt = 0
                        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            ni, nj = i + di, j + dj
                            if a[ni][nj] == 0:
                                cnt += 1
                        if arr[i][j] - cnt <= 0:
                            arr[i][j] = 0
                        else:
                            arr[i][j] -= cnt
        elif count == 0:
            print(0)
            break
        else:
            print(k)
            break

