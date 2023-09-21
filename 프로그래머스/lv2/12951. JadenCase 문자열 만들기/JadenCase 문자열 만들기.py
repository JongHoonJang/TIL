def solution(s):
    answer = ''
    s = s.lower()
    m = list(s.split())
    i = 0
    while i < len(s):
        if s[i] == ' ':
            answer += ' '
            i += 1
        else:
            k = m.pop(0)
            if 96 < ord(k[0]) < 123:
                answer += chr(ord(k[0]) - 32) + k[1:]
            else:
                answer += k
            i += len(k)
            
    
    return answer