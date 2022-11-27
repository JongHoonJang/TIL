def BFS(si, sj):
    queue = [(si, sj)]
    visited = [[0] * M for _ in range(N)]
    while queue:
        y, x = queue.pop(0)
        if not visited[y][x]:
            visited[y][x] = 1
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M:
                if arr[ny][nx] != '#' and not visited[ny][nx]:
                    queue.append((ny, nx))
                    visited[ny][nx] = visited[y][x] + 1
    else:
        q = []
        for p in point:
            q.append(visited[p[0]][p[1]] - 1)
        return q


T = int(input())
for t in range(1, T + 1):
    M, N = map(int, input().split())
    arr = [input() for _ in range(N)]
    lst = []
    point = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'A':
                point.append((i, j))
            elif arr[i][j] == 'S':
                point.insert(len(point), (i, j))
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'A' or arr[i][j] == 'S':
                lst.append(BFS(i, j))
    key = [9999999] * (len(lst))
    visit = [0] * (len(lst))
    key[0] = 0
    cnt = 0
    while cnt < len(lst):
        min_value = 9999999
        for i in range(len(lst)):
            if not visit[i] and key[i] < min_value:
                min_value = key[i]
                u = i
        visit[u] = 1
        for w in range(len(lst)):
            if lst[u][w] > 0 and not visit[w]:
                if key[w] > lst[u][w]:
                    key[w] = lst[u][w]
        cnt += 1
    print(f'{sum(key)}')