def solution(targets):
    answer = 0
    k = 0
    for s, e in sorted(targets):
        if k > s:
            k = min(k, e)
        else:
            k = e
            answer += 1
        
    return answer