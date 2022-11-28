import sys
sys.stdin = open("오셀로_input.txt")


def over(a, b):
    if 0 <= a <= N and 0 <= b <= N:
        return True
    return False


T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    bode = [[0] * (N + 1) for _ in range(N + 1)]
    start = N // 2
    bode[start][start] = bode[start + 1][start + 1] = 2
    bode[start + 1][start] = bode[start][start + 1] = 1
    for m in range(M):
        x, y, st = map(int, input().split())
        bode[y][x] = st
        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)):
            revers = []
            for k in range(1, N):
                new_y = y + dy * k
                new_x = x + dx * k
                if over(new_y, new_x):
                    if bode[new_y][new_x] == 0:
                        break
                    elif bode[new_y][new_x] == st:
                        for ry, rx in revers:
                            bode[ry][rx] = st
                        break
                    else:
                        revers.append((new_y, new_x))
                else:
                    break
    wst = 0
    bst = 0
    for bd in bode:
        wst += bd.count(2)
        bst += bd.count(1)
    print(f'#{t} {bst} {wst}')
