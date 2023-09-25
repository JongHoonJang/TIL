def solution(s):
    answer = ''
    k = 0
    if s[0] == ' ':
        for j in range(k, len(s)):
            if s[j] == ' ':
                answer += ' '
            else:
                k = j
                break
    for data in s.split():
        for i in range(len(data)):
            if i % 2:
                answer += data[i].lower()
            else:
                answer += data[i].upper()
        else:
            k += len(data)
            for j in range(k, len(s)):
                if s[j] == ' ':
                    answer += ' '
                else:
                    k = j
                    break
    return answer