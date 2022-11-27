import sys

sys.stdin = open("파리퇴치_input.txt")

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    fly = [list(map(int, input().split())) for _ in range(N)]
    max_clear = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            clear = 0
            for mi in range(M):
                for mj in range(M):
                    clear += fly[mi + i][mj + j]
            if max_clear < clear:
                max_clear = clear
    print(f'#{t} {max_clear}')
