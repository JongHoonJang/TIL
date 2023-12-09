def solution(operations):
    answer = []
    for oper in operations:
        op, num = oper.split()
        if op == 'I':
            answer.append(int(num))
        if op == 'D' and answer != []:
            if num == '1':
                answer.pop(answer.index(max(answer)))
            else:
                answer.pop(answer.index(min(answer)))

    if answer == []:
        return [0, 0]
    return [max(answer), min(answer)]