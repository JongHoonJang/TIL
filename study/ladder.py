import sys

sys.stdin = open("ladder_input.txt")

for t in range(1, 11):
    n = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    x_p = 0
    y_p = 99

    for i in range(100):
        if ladder[y_p][i] == 2:
            x_p = i
    while y_p > 0:
        if 0 < x_p and ladder[y_p][x_p - 1]:
            for x in range(x_p, 0, -1):
                if ladder[y_p][x_p - 1]:
                    x_p = x - 1
            y_p -= 1
        elif x_p < 99 and ladder[y_p][x_p + 1]:
            for x in range(x_p, 99):
                if ladder[y_p][x_p + 1]:
                    x_p = x + 1
            y_p -= 1
        else:
            y_p -= 1

    print(f'#{t} {x_p}')
