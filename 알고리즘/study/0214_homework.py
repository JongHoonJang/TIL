import sys

sys.stdin = open("sum_input.txt")

for T in range(1, 11):
    t = input()
    paper = [list(map(int, input().split())) for i in range(100)]
    result = []
    value_cross1 = value_cross2 = 0
    for i in range(100):
        value_x = 0
        value_y = 0
        for j in range(100):
            value_x += paper[i][j]
            value_y += paper[j][i]
            if i == j:
                value_cross1 += paper[i][j]
                value_cross2 += paper[i][-(j + 1)]
        result.extend([value_x, value_y])
    result.extend([value_cross1, value_cross2])

    max_value = result[0]
    for value in result:
        if max_value < value:
            max_value = value
    print(f'#{t} {max_value}')
