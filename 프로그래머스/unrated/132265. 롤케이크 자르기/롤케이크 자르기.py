from collections import Counter
def solution(topping):
    answer = 0
    b = Counter(topping)
    c = set()
    for i in topping:
        b[i] -= 1
        if b[i] == 0:
            del b[i]
        c.add(i)
        if len(b) == len(c):
            answer += 1
    return answer