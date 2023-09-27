def solution(s):
    answer = ''
    res = []
    for i in s:
        res.append(ord(i))
    res.sort(reverse=True)
    for j in res:
        answer += chr(j)
    return answer