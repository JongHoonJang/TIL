import sys
sys.stdin = open("정사각형input.txt")


def over(a, b):
    if 0 <= a < N and 0 <= b < N:
        return False
    return True


def BFS(yi, xj):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = [(yi, xj)]
    cnt = 1
    while queue:
        now_y, now_x = queue.pop(0)
        for d in range(4):
            y = now_y + dy[d]
            x = now_x + dx[d]
            if over(y, x):
                continue
            elif room[y][x] - room[now_y][now_x] == 1:
                queue.append((y, x))
                cnt += 1
    return cnt


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    result = []
    max_cnt = 0
    min_value = 0
    for i in range(N):
        for j in range(N):
            value = BFS(i, j)
            if max_cnt < value:
                max_cnt = value
                min_value = room[i][j]
            elif max_cnt == value:
                if min_value > room[i][j]:
                    min_value = room[i][j]

    print(f'#{t} {min_value} {max_cnt}')
