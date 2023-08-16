def solution(a, b, n):
    answer = 0
    while n >= a:
        t = 0
        answer += (n // a) * b
        if n % a:
            t = (n % a)
        n //= a
        n *= b
        n += t
    return answer