def BFS(s, c):
    queue = [(s[0], s[1], c)]
    visited[s[0]][s[1]] = 0
    while queue:
        y, x, cnt = queue.pop(0)
        for dy, dx in move:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N:
                if visited[ny][nx] > cnt + 1:
                    queue.append((ny, nx, cnt + 1))
                    visited[ny][nx] = cnt + 1


move = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
T = int(input())
for t in range(T):
    N = int(input())
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
    visited = [[99999999] * N for _ in range(N)]
    BFS(start, 0)
    print(visited[end[0]][end[1]])
