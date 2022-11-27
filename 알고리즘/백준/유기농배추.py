def BFS(a, b):
    queue = [(a, b)]
    while queue:
        now_y, now_x = queue.pop(0)
        if not visited[now_y][now_x]:
            visited[now_y][now_x] = 1
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_y, new_x = now_y + dy, now_x + dx
            if 0 <= new_y < N and 0 <= new_x < M:
                if arr[new_y][new_x] == 1 and not visited[new_y][new_x]:
                    queue.append((new_y, new_x))
                    visited[new_y][new_x] = 1


T = int(input())
for t in range(T):
    M, N, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    for k in range(K):
        x, y = map(int, input().split())
        arr[y][x] = 1
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and not visited[i][j]:
                BFS(i, j)
                cnt += 1
    print(cnt)