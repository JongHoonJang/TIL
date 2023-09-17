def solution(s, n):
    answer = ''
    # 65 90 97 122
    for i in s:
        if i == ' ':
            answer += ' '
        else:
            k = ord(i) + n
            if ord(i) < 91 and k > 90:
                k -= 26
            elif ord(i) < 123 and k > 122:
                k -= 26
            answer += chr(k)
                           

    return answer