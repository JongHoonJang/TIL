def solution(i, j, k):
    answer = 0
    for a in range(i,j+1):
        for b in str(a):
            answer += b.count(str(k))
    return answer