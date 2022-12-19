def over(a, b):
    if 0 <= a < N and 0 <= b < M:
        return True
    return False


def BFS(v):
    global res
    queue = v
    while queue:
        y, x = queue.pop(0)
        if not v_lst[y][x]:
            v_lst[y][x] = 1
        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            new_y, new_x = y + dy, x + dx
            if over(new_y, new_x):
                if not arr[new_y][new_x] and not v_lst[new_y][new_x]:
                    queue.append((new_y, new_x))
                    v_lst[new_y][new_x] = 1
    else:
        cnt = 0
        for r in range(N):
            for c in range(M):
                if v_lst[r][c] == 0:
                    cnt += 1
        if res < cnt:
            res = cnt


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
virus = []
lst = []
res = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            visited[i][j] = 1
        elif arr[i][j] == 0:
            lst.append((i, j))
        else:
            virus.append((i, j))

for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        for k in range(j + 1, len(lst)):
            v_lst = [data[:] for data in visited]
            virus_lst = virus[:]
            v_lst[lst[i][0]][lst[i][1]] = 1
            v_lst[lst[j][0]][lst[j][1]] = 1
            v_lst[lst[k][0]][lst[k][1]] = 1
            BFS(virus_lst)
print(res)