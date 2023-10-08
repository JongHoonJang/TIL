def solution(dartResult):
    answer = []
    i = 0
    while i < len(dartResult):
        if dartResult[i:i + 2] == '10':
            answer.append(10)
            i += 2
        elif dartResult[i] in ['0','1','2','3','4','5','6','7','8','9']:
            answer.append(int(dartResult[i]))
            i += 1
        elif dartResult[i] in ['S', 'D', 'T']:
            if dartResult[i] == 'D':
                if answer[-1] < 0:
                    answer[-1] = -(answer[-1] ** 2)
                else:
                    answer[-1] = answer[-1] ** 2
            elif dartResult[i] == 'T':
                if answer[-1] < 0:
                    answer[-1] = -(answer[-1] ** 3)
                else:
                    answer[-1] = answer[-1] ** 3
            i += 1
        elif dartResult[i] in ['*', '#']:
            if dartResult[i] == '*':
                answer[-2:] = list(map(lambda x : x * 2, answer[-2:]))
            else:
                answer[-1] = -answer[-1]
            i += 1

    return sum(answer)