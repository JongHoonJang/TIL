def solution(n):
    answer = 0
    for i in range(n, 0, -1):
        if n % 2:
            if i % 2:
                answer += i
        else:
            if i % 2 == 0:
                answer += i ** 2
    return answer