def solution(k, tangerine):
    answer = 0
    orange = {}
    for t in tangerine:
        if t not in orange:
            orange[t] = 1
        else:
            orange[t] += 1
    orange1 = sorted(orange.items(), key = lambda x: -x[1])
    for a, b in orange1:
        if k - b <= 0:
            answer += 1
            break
        else:
            answer += 1
            k -= b
    return answer