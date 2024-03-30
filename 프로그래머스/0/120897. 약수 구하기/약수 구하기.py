def solution(n):
    answer = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            answer.extend([i, n // i])
    answer = set(answer)
    return sorted(list(answer))