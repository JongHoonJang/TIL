def solution(n, m):
    answer = [0,n * m]
    for i in range(1, n * m + 1):
        if n % i == 0 and m % i == 0:
            answer[0] = i
        elif i % n == 0 and i % m == 0:
            if answer[1] > i:
                answer[1] = i
    return answer