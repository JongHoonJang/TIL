def solution(maps):
    answer = []
    def bfs(i, j):
        queue = [(i, j)]
        food = 0
        while queue:
            yy, xx = queue.pop(0)
            if visited[yy][xx] == 0:
                visited[yy][xx] = 1
            food += int(maps[yy][xx])
            for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ny, nx = yy + dy, xx + dx
                if 0 <= ny < y_len and 0 <= nx < x_len:
                    if maps[ny][nx] != 'X' and visited[ny][nx] == 0:
                        visited[ny][nx] = 1
                        queue.append((ny,nx))
                        
        else:

            return food
        
        
    x_len = len(maps[0])
    y_len = len(maps)
    visited = [[0] * x_len for _ in range(y_len)]
    for y in range(y_len):
        for x in range(x_len):
            if maps[y][x] != 'X' and visited[y][x] == 0:
                answer.append(bfs(y, x))
    if len(answer):
        answer.sort()
    else:
        answer.append(-1)
    return answer