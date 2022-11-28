import sys
sys.stdin = open("myroom_input.txt")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    room = [0] * 201  # 0~201 = 0 + 1~200
    for _ in range(N):
        p1, p2 = map(int, input().split())
        if p1 > p2:
            p1, p2 = p2, p1
        p1 = (p1 + 1) // 2
        p2 = (p2 + 1) // 2
        for i in range(p1, p2 + 1):
            room[i] += 1
    print(f'#{tc} {max(room)}')





