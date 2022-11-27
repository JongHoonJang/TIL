import sys

sys.stdin = open("낱말퍼즐_input.txt")

T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    for i in range(N):
        cnt_x = 0
        cnt_y = 0
        for j in range(N):
            if puzzle[i][j]:
                cnt_x += 1
            if puzzle[j][i]:
                cnt_y += 1
            if puzzle[i][j] == 0 or j == N - 1:
                if cnt_x == K:
                    count += 1
                cnt_x = 0
            if puzzle[j][i] == 0 or j == N - 1:
                if cnt_y == K:
                    count += 1
                cnt_y = 0
    print(f"#{t} {count}")


