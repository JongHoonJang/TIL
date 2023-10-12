def solution(n):
    answer = 2
    b = 1
    c = 0
    for i in range(n - 2):
        c = answer
        answer += b
        b = c
    
    return answer % 1000000007