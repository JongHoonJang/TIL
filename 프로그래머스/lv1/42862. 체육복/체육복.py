def solution(n, lost, reserve):
    answer = 0
    res = []
    for i in lost:
        if i in reserve:
            res.append(i)
    for i in range(1, n + 1):
        if i in lost and i not in res:
            if i - 1 in reserve and i - 1 not in res:
                answer += 1
                reserve.pop(reserve.index(i - 1))
            elif i + 1 in reserve and i + 1 not in res:
                answer += 1
                reserve.pop(reserve.index(i + 1))
        else:
            answer += 1
    return answer