def solution(maps):
    x = len(maps[0])
    y = len(maps)
    visited = [[0] * x for _ in range(y)]
    queue = [(0,0)]
    visited[0][0] = 1
    while queue:
        ny, nx = queue.pop(0)
        
        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            yy, xx = ny + dy, nx + dx
            if 0 <= yy < y and 0 <= xx < x:
                if maps[yy][xx] == 1 and visited[yy][xx] == 0:
                    queue.append((yy,xx))
                    visited[yy][xx] = visited[ny][nx] + 1
    if visited[y - 1][x - 1]:
        return visited[y - 1][x - 1]
    else:
        return -1