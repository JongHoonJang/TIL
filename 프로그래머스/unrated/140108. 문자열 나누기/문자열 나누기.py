def solution(s):
    answer = 0
    x = ''
    not_x = ''
    for i in s:
        if x == '' or x[0] == i:
            x += i
        else:
            not_x += i
        if len(x) == len(not_x):
            answer += 1
            x = ''
            not_x = ''
    else:
        if x or not_x:
            answer += 1
    return answer