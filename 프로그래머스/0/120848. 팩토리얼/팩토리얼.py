def solution(n):
    answer = 1
    for i in range(1, 12):
        answer *= i
        if answer > n:
            return i - 1

