def over(a, b):
    if 0 <= a < N and 0 <= b < N:
        return True
    return False


def BFS(y, x):
    queue = [(y, x)]
    visited[y][x] = int(arr[y][x])
    while queue:
        now_y, now_x = queue.pop(0)
        for dy, dx in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
            new_y, new_x = now_y + dy, now_x + dx
            if over(new_y, new_x):
                if visited[new_y][new_x] > visited[now_y][now_x] + int(arr[new_y][new_x]):
                    queue.append((new_y, new_x))
                    visited[new_y][new_x] = visited[now_y][now_x] + int(arr[new_y][new_x])

    return visited[N-1][N-1]


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [input() for _ in range(N)]
    visited = [[99999999] * N for _ in range(N)]
    print(f'#{t} {BFS(0, 0)}')
