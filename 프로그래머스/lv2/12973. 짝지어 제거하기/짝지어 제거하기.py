from collections import deque
def solution(s):
    answer = 1
    k = deque()
    for i in s:
        k.append(i)
        if len(k) > 1:
            if k[-1] == k[-2]:
                k.pop()
                k.pop()
    if len(k):
        answer = 0

    return answer