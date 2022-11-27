from collections import deque


def check(v):
    for num in v:
        for n in num:
            if n == 0:
                return False
    return True


def BFS(p):
    global brk, res
    queue = deque()
    queue.append((0, 0))
    v_lst = [data[:] for data in bode]
    v_lst[p[0]][p[1]] = 0
    while queue:
        y, x = queue.popleft()
        if not v_lst[y][x]:
            v_lst[y][x] = 1
        if res <= v_lst[y][x] + 1:
            break
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M:
                if v_lst[ny][nx] == 0 and not v_lst[ny][nx]:
                    queue.append((ny, nx))
                    v_lst[ny][nx] = v_lst[y][x] + 1

    else:
        if check(v_lst):
            brk = 0
            return v_lst[N - 1][M - 1]
        else:
            return 9999999999


N, M = map(int, input().split())
arr = [input() for _ in range(N)]
bode = [[0] * M for _ in range(N)]
lst = []
res = 9999999999
brk = 1
for i in range(N):
    for j in range(M):
        if arr[i][j] == '1':
            bode[i][j] = 1
            lst.append((i, j))
for i in range(len(lst)):
    value = BFS(lst[i])
    if brk == 0 and value > 0:
        if res > value:
            res = value
    else:
        res = -1
print(res)
