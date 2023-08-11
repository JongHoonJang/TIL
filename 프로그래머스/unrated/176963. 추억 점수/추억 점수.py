def solution(name, yearning, photo):
    answer = []
    arr = {}
    for i in range(len(name)):
        arr[name[i]] = yearning[i]
    for lst in photo:
        res = 0
        for j in lst:
            if j in name:
                res += arr[j]
        answer.append(res)
                
    return answer