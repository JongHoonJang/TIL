def solution(s):
    answer = []
    arr = []
    for i in s:
        if i not in arr:
            arr.append(i)
            answer.append(-1)
        elif i in arr:
            j = 1
            while True:
                if arr[-j] == i:
                    arr.append(i)
                    answer.append(j)
                    break
                j += 1
        
    return answer