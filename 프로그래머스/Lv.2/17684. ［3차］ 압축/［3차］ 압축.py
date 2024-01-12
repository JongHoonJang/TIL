def solution(msg):
    answer = []
    dic = {}
    k = 1
    for i in range(65, 91):
        dic[chr(i)] = k
        k += 1
    j = 0
    if len(msg) == 1:
        return [dic[msg]]
    while j < len(msg):
        answer.append(0)
        for l in range(1, len(msg)):
            if j + l == len(msg) and msg[j : j + l] in dic:
                answer[-1] = dic[msg[j : j + l]]
                j += l
                break
            elif msg[j : j + l] in dic:
                answer[-1] = dic[msg[j : j + l]]
                l += 1
            elif msg[j : j + l] not in dic:
                dic[msg[j : j + l]] = k
                k += 1
                j += l - 1
                break
            
    return answer