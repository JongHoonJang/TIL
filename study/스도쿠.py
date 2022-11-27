import sys
sys.stdin = open("스도쿠_input.txt")

T = int(input())

for t in range(1, T + 1):
    puzzle = [list(map(int, input().split())) for _ in range(9)]
    result = 0
    for i in range(9):
        value_x = 0
        value_y = 0
        for j in range(9):
            value_x += puzzle[i][j]
            value_y += puzzle[j][i]
        if value_y != 45 or value_x != 45:
            break
    else:
        for x in range(0, 7, 3):
            for y in range(0, 7, 3):
                value = 0
                for m in range(3):
                    for n in range(3):
                        value += puzzle[m + x][n + y]
            if value != 45:
                break
        else:
            result = 1
    print(f'#{t} {result}')

