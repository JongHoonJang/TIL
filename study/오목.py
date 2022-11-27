import sys
sys.stdin = open("오목_input.txt")


def result(arr):
    dr = [0, 1, 1, 1]
    dc = [1, 0, 1, -1]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                for d in range(4):
                    r, c = i, j
                    cnt = 0
                    while 0 <= r < N and 0 <= c < N and arr[r][c] == 'o':
                        cnt += 1
                        r += dr[d]
                        c += dc[d]
                        if cnt >= 5:
                            return 'YES'
    return 'NO'


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    lst = [list(input()) for _ in range(N)]
    print(f'#{t} {result(lst)}')

