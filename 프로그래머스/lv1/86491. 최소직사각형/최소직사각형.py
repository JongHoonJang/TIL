def solution(sizes):
    w = 0
    h = 0
    for s in sizes:
        if w < min(s):
            w = min(s)
        if h < max(s):
            h = max(s)
    
    return w * h