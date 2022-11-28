def BFS(s):
    queue = [(s[0], s[1])]

    while queue:
        y, x = queue.pop(0)
        if not visited[y][x]:
            visited[y][x] = 1
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M:
                if arr[ny][nx] != 0 and not visited[ny][nx]:
                    queue.append((ny, nx))
                    visited[ny][nx] = visited[y][x] + 1


T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    start = list(map(int, input().split()))
    day = [0] * 10000001
    visited = [[0] * M for _ in range(N)]
    BFS(start)
    i = 1
