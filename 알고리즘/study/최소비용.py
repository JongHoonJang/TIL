def over(a, b):
    if 0 <= a < N and 0 <= b < N:
        return True
    return False


def BFS(y, x):
    visited = [[99999999999] * N for _ in range(N)]
    queue = [(y, x)]
    visited[y][x] = 0
    while queue:
        now_y, now_x = queue.pop(0)
        for dy, dx in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
            new_y, new_x = now_y + dy, now_x + dx
            if over(new_y, new_x):
                up = 1
                if arr[new_y][new_x] > arr[now_y][now_x]:
                    up += arr[new_y][new_x] - arr[now_y][now_x]
                if visited[new_y][new_x] > visited[now_y][now_x] + up:
                    queue.append((new_y, new_x))
                    visited[new_y][new_x] = visited[now_y][now_x] + up

    return visited[N-1][N-1]


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{t} {BFS(0, 0)}')


