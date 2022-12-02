def over(y, x):
    if 0 <= y < n and 0 <= x < m:
        return False
    return True


def BFS(y, x):
    stack = [(y, x)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    while stack:
        y_now, x_now = stack.pop(0)
        if not visited[y_now][x_now]:
            visited[y_now][x_now] = 1
        for d in range(4):
            x = x_now + dx[d]
            y = y_now + dy[d]
            if over(y, x):
                continue
            elif miro[y][x] == 1:
                if not visited[y][x]:
                    stack.append((y, x))
                    visited[y][x] = visited[y_now][x_now] + 1
    return visited[n-1][m-1]


n, m = map(int, input().split())
miro = [([0] * m) for _ in range(n)]
for i in range(n):
    lst = input()
    for j in range(m):
        miro[i][j] = int(lst[j])
visited = [([0] * m) for _ in range(n)]
print(BFS(0, 0))


