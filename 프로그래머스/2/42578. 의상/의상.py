def solution(clothes):
    answer = 1
    dic = {}
    for data in clothes:
        if data[1] not in dic:
            dic[data[1]] = [data[0]]
        else:
            dic[data[1]].append(data[0])
    for v in dic.values():
        answer *= (len(v) + 1)

    return answer - 1
