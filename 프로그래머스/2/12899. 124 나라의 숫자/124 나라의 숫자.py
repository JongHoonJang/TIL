def solution(n):
    answer = []
    while n:
        t = n % 3
        if not t:
            t = 3
            n -= 1
        answer.append(str(t))
        n //= 3
    for i in range(len(answer)):
        if answer[i] == '3':
            answer[i] = '4'
    return ''.join(answer[::-1])