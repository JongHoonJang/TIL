def solution(N, stages):
    answer = []
    res = []
    k = len(stages)
    for i in range(1, N + 1):
        c = stages.count(i)
        if c == 0:
            res.append([i, 0])
        else:
            res.append([i, c / k])
        k -= c
    res.sort(key=lambda x : -x[1])
    for r, _ in res:
        answer.append(r)
    return answer