def solution(s):
    if 4 != len(s) and 6 != len(s):
        return False
    for i in s:
        if i not in [str(j) for j in range(10)]:
            return False
    return True