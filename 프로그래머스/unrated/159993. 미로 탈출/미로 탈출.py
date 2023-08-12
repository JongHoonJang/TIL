from collections import deque
def solution(maps):
    answer = 0
    y = len(maps)
    x = len(maps[0])
    l_que = deque()
    e_que = deque()
    l_visited = [[0] * x for _ in range(y)]
    e_visited = [[0] * x for _ in range(y)]
    for i in range(y):
        for j in range(x):
            if maps[i][j] == 'S':
                l_que.append((i, j))
                break
        if l_que:
            break
    while l_que:
        ny, nx = l_que.popleft()
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_y, new_x = ny + dy, nx + dx
            if 0 <= new_y < y and 0 <= new_x < x:
                if maps[new_y][new_x] == 'L':
                    e_que.append((new_y,new_x))
                    e_visited[new_y][new_x] = l_visited[ny][nx] + 1
                elif maps[new_y][new_x] != 'X':
                    if l_visited[new_y][new_x] == 0:
                        l_que.append((new_y, new_x))
                        l_visited[new_y][new_x] = l_visited[ny][nx] + 1
        if e_que:
            break
    else:
        answer = -1

    if e_que:       
        while e_que:

            ny, nx = e_que.popleft()
            for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_y, new_x = ny + dy, nx + dx
                if 0 <= new_y < y and 0 <= new_x < x:
                    if maps[new_y][new_x] == 'E':
                        answer = e_visited[ny][nx] + 1
                    elif maps[new_y][new_x] != 'X':
                        if e_visited[new_y][new_x] == 0:
                            e_que.append((new_y, new_x))
                            e_visited[new_y][new_x] = e_visited[ny][nx] + 1
            if answer != 0:
                break
        else:
            answer = -1
        
    return answer