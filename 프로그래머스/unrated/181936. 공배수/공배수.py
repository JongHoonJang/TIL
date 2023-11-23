def solution(number, n, m):
    if number % n or number % m:
        return 0
    return 1