T = int(input())

for t in range(T):
    score = input()
    i = 0
    num = 1
    result = 0
    while i < len(score):
        if score[i] == 'O':
            if score[i - 1] == 'O' and i > 0:
                num += 1
            else:
                num = 1
            result += num
        else:
            num = 1
        i += 1

    print(result)

