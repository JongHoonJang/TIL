def solution(n):
    answer = -1
    for i in range(1,10000000):
        if i ** 2 == n:
            answer = (i + 1) ** 2
            break
    return answer