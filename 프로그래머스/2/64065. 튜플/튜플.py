def solution(s):
    answer = []
    dic = {}
    num = ''
    for data in s:
        if data in ['1','2','3','4','5','6','7','8','9','0']:
            num += data
        else:
            if num != '':

                if num not in dic:
                    dic[num] = 1
                else:
                    dic[num] += 1
            num = ''
    dic = sorted(dic.items(), key=lambda x : x[1], reverse=True)
    for d in dic:
        answer.append(int(d[0]))
    return answer