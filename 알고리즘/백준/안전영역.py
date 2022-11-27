def BFS(y, x):
    queue = [(y, x)]
    while queue:
        ny, nx = queue.pop(0)
        if not visited[ny][nx]:
            visited[ny][nx] = 1
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_y, new_x = ny + dy, nx + dx
            if 0 <= new_y < N and 0 <= new_x < N:
                if arr[new_y][new_x] >= h and not visited[new_y][new_x]:
                    queue.append((new_y, new_x))
                    visited[new_y][new_x] = 1


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
world = [0] * 101

for h in range(1, 101):
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] >= h and not visited[i][j]:
                BFS(i, j)
                cnt += 1
    world[h] = cnt

print(max(world))
