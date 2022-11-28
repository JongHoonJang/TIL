import sys

sys.stdin = open("vertical_input.txt")

T = int(input())

for t in range(1, T + 1):
    words = [input() for _ in range(5)]
    result = ''

    # for i in range(len(words)):
    #     if len(words[i]) < 15:
    #         words[i] += ' ' * (15 - len(words[i]))
    # for i in range(15):
    #     for j in range(5):
    #         if words[j][i] != ' ':
    #             result += words[j][i]

    for j in range(15):
        for i in range(5):
            if j < len(words[i]):
                result += words[i][j]
    print(f'#{t} {result}')
