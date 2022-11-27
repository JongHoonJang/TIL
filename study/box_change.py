import sys
sys.stdin = open("box_change_input.txt")

T = int(input())
for tc in range(1, T + 1):
    N, Q = map(int, input().split())
    num = [list(map(int, input().split())) for _ in range(Q)]
    box = [0] * N

    for i in range(Q):
        for j in range(num[i][0], num[i][1] + 1):
            box[j - 1] = i + 1

    print(f'#{tc}', *box)

