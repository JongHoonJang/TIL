def solution(s):
    n = len(s)
    answer = n
    for i in range(1, n):
        w = ''
        res = ''
        cnt = 1
        j = 0
        while j < n:
            if i + j > n:
                res += s[j: n + 1]
            elif w != s[j:j+i]:
                if cnt > 1:
                    res += str(cnt) + w
                    cnt = 1
                else:
                    res += w
                w = s[j:j+i]
            elif w == s[j:j+i]:
                cnt += 1
            
            j += i
        else:
            if cnt > 1:
                    res += str(cnt) + w
                    cnt = 1
            else:
                res += w
            if answer > len(res):
                answer = len(res)

    return answer