def solution(n):
    answer = 0
    res = ''
    while n > 0:
        res = str(n % 3) + res
        n //= 3
    for i in range(len(res)):
        answer += int(res[i]) * (3 ** i)

    return answer