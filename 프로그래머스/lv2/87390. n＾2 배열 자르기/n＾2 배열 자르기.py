
def solution(n, left, right):
    answer = []
    l = left // n
    r = right // n + 1
    res = list(range(1, n + 1))
    ls = left % n
    re = right - n * l
    for i in range(l, r):
        if i != 0:
            res[:i] = [i + 1] * i
        answer.extend(res)
        
    return answer[ls: re + 1]