def solution(s):
    answer = [0, 0]
    while s != '1':
        l = len(s)
        s = s.replace('0','')
        k = len(s)
        answer[0] += 1
        answer[1] += l - k
        new_s = ''
        while k > 0:
            new_s += str(k % 2)
            k //= 2
        else:
            s = new_s
            
    return answer