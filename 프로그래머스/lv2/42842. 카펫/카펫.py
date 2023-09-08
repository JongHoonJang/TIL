def solution(brown, yellow):
    b = brown + yellow
    w = 3
    h = 1
    while True:
        h = b // w
        if b % w == 0 and w >= h and yellow == (w - 2) * (h - 2):
            return [w, h]
        w += 1