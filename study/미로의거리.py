import sys
sys.stdin = open("미로찾기_input.txt")


def over(y, x):
    if 0 <= y < N and 0 <= x < N:
        return False
    return True


def BFS(y, x):
    global value
    stack = [(y, x)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    while stack:
        y_now, x_now = stack.pop(0)
        for d in range(4):
            x = x_now + dx[d]
            y = y_now + dy[d]
            if over(y, x):
                continue
            elif miro[y][x] == 0:
                if not visited[y][x]:
                    stack.append((y, x))
                    visited[y][x] = visited[y_now][x_now] + 1
            elif miro[y][x] == 3:
                value.append(visited[y_now][x_now])


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    miro = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    value = []
    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                BFS(i, j)
    if len(value) == 0:
        cnt = 0
    else:
        cnt = min(value)
    print(f'#{t} {cnt}')
