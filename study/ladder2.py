import sys
sys.stdin = open("ladder2_input.txt")


def count(x):
    y = 0
    cnt = 1
    while y < 99:
        if 0 < x < 100 and ladder[y][x - 1]:
            while 0 < x < 100 and ladder[y][x - 1]:
                x -= 1
                cnt += 1
            else:
                y += 1
        elif -1 < x < 99 and ladder[y][x + 1] == 1:
            while -1 < x < 99 and ladder[y][x + 1] == 1:
                x += 1
                cnt += 1
            else:
                y += 1
        else:
            y += 1
    else:
        return cnt


for tc in range(0, 10):
    t = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    start_idx = []
    result = []
    for i in range(100):
        if ladder[0][i]:
            start_idx.append(i)
    for x_p in start_idx:
        result.append(count(x_p))

    print(f'#{t} {start_idx[result.index(min(result))]}')
