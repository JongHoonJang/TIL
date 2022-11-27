def over(a, b):
    if 0 <= a < N and 0 <= b < N:
        return False
    return True

def BFS(y, x):
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    queue = [(y, x)]
    visit_bfs = []
    while queue:
        now_y, now_x = queue.pop(0)
        sol[now_y][now_x] = 0
        visit_bfs.append((now_y, now_x))
        for d in range(4):
            x = now_x + dx[d]
            y = now_y + dy[d]
            if over(y, x):
                continue
            elif (y, x) not in visit_bfs and sol[y][x] == 1:
                queue.append((y, x))
                sol[y][x] = 0
    else:
        return len(visit_bfs)


N = int(input())

lst = [input() for _ in range(N)]
sol = [[] for _ in range(N)]
idx = 0
result = []
for string in lst:
    for s in string:
        sol[idx].append(int(s))
        if len(sol[idx]) == N:
            idx += 1
for i in range(N):
    for j in range(N):
        if sol[i][j] == 1:
            visited = [([0] * N) for _ in range(N)]
            result.append(BFS(i, j))
print(len(result))
result.sort()
for p in result:
    print(p)


