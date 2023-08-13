def solution(s, skip, index):
#     a = 97 z = 122
    answer = ''
    n = []
    for p in skip:
        n.append(ord(p))
    for i in s:
        k = ord(i)
        j = 1
        while j <= index:
            if k + 1 > 122:
                k -= 26
            if k + 1 in n:
                k += 1
            elif k + 1 not in n:
                k += 1
                j += 1

        answer += chr(k)
                
            
    return answer