from collections import deque


def result():
    value = 0
    for i in range(Z):
        for j in range(Y):
            for k in range(X):
                if value < arr[i][j][k]:
                    value = arr[i][j][k]
                if arr[i][j][k] == 0:
                    return -1
    else:
        return value


def BFS(mato):
    queue = deque(mato)

    while queue:
        zz, yy, xx = queue.popleft()
        for dz, dy, dx in [(0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1), (1, 0, 0), (-1, 0, 0)]:
            nz, ny, nx = zz + dz, yy + dy, xx + dx
            if 0 <= nz < Z and 0 <= ny < Y and 0 <= nx < X:
                if arr[nz][ny][nx] == 0:
                    queue.append((nz, ny, nx))
                    arr[nz][ny][nx] = arr[zz][yy][xx] + 1


X, Y, Z = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(Y)] for _ in range(Z)]
find = []
for z in range(Z):
    for y in range(Y):
        for x in range(X):
            if arr[z][y][x] == 1:
                find.append((z, y, x))

BFS(find)
res = result()
if res == -1:
    print(-1)
else:
    print(res - 1)
