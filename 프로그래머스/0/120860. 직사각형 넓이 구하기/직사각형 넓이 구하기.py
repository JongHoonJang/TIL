def solution(dots):
    x = [i[0] for i in dots]
    y = [j[1] for j in dots]
    a = max(x) - min(x)
    b = max(y) - min(y)
    return a * b