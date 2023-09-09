def solution(d, budget):
    answer = 0
    d.sort()
    for i in range(len(d)):
        if budget - d[i] >= 0:
            budget -= d[i]
        else: 
            return i
    else:
        return len(d)