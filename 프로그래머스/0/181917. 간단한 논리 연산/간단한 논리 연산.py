def solution(x1, x2, x3, x4):
    answer = True
    if x1 or x2:
        if x3 or x4:
            return True
    return False