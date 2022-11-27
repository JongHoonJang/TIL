import sys
sys.stdin = open("IM예제")


def over(a, b):
    if 0 <= a < N and 0 <= b < N:
        return False
    return True


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    lst = [list(input()) for _ in range(N)]

    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if lst[i][j] == 'H':
                for d in range(4):
                    x = j + dx[d]
                    y = i + dy[d]
                    if over(y, x):
                        continue
                    elif lst[y][x] == 'A':
                        break
                else:
                    cnt += 1
    print(f'#{t} {cnt}')
