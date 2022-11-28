import sys
sys.stdin = open("미로찾기_input.txt")


def over(a, b):
    if 0 <= a < N and 0 <= b < N:
        return False
    return True


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    mero = [list(map(int, input())) for _ in range(N)]
    visit = [[0] * N for _ in range(N)]
    result = 0
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    for i in range(N):
        for j in range(N):
            if mero[i][j] == 2:
                stack = [(i, j)]
            if mero[i][j] == 1:
                visit[i][j] = 1
    while stack:
        now_y, now_x = stack.pop()
        visit[now_y][now_x] = 1
        if mero[now_y][now_x] == 3:
            result = 1
            break
        for d in range(4):
            x = now_x + dx[d]
            y = now_y + dy[d]
            if over(y, x):
                continue
            elif visit[y][x] == 0:
                stack.append((y, x))
    print(f'#{t} {result}')
