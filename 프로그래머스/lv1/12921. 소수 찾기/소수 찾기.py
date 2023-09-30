import math
def solution(n):
    answer = [1] * (n + 1)

    for i in range(2, int(math.sqrt(n))+1):
        if answer[i]:
            j = 2
            while i * j <= n:
                answer[i * j] = 0
                j += 1
    return sum(answer) - 2