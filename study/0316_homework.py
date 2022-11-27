import sys
sys.stdin = open("0316homework")


def over(a, b):
    if 0 <= a < 16 and 0 <= b < 16:
        return False
    return True


def BFS(y,x):
    queue = [(y,x)]
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    while queue:
        now_y, now_x = queue.pop(0)
        if not miro1[now_y][now_x]:
            miro1[now_y][now_x] = 1
        for d in range(4):
            next_x = now_x + dx[d]
            next_y = now_y + dy[d]
            if over(next_y, next_x):
                continue
            elif miro1[next_y][next_x] == 3:
                return 1
                break
            elif miro1[next_y][next_x] == 0:
                queue.append((next_y, next_x))
                miro1[next_y][next_x] = 1
    else:
        return 0


for t in range(10):
    T = int(input())
    miro = [input() for _ in range(16)]
    miro1 = [[0]*16 for _ in range(16)]
    for i in range(16):
        for j in range(16):
            miro1[i][j] = int(miro[i][j])
    print(f'#{T} {BFS(1, 1)}')
