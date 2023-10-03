def solution(s):
    answer = ''
    if len(s) % 2:
        return s[len(s)//2]
    return s[len(s)//2 - 1:len(s)//2 + 1]