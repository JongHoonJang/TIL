from collections import deque


def BFS(mato):
    queue = deque(mato)

    while queue:
        y, x = queue.popleft()
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M:
                if arr[ny][nx] == 0:
                    queue.append((ny, nx))
                    arr[ny][nx] = arr[y][x] + 1


M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
find = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            find.append((i, j))

BFS(find)
flag = 0
res = 0
for a in arr:
    if res < max(a):
        res = max(a)
    if a.count(0) > 0:
        res = 0
        break
print(res - 1)