def solution(citations):
    answer = 0

    for i in range(len(citations) + 1):
        l = m = 0
        for c in citations:
            if i <= c:
                m += 1
            else:
                l += 1
        if i <= m and i >= l:
            if answer < i:
                answer = i
        
    return answer